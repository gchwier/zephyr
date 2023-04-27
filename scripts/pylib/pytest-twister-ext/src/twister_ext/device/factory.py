from __future__ import annotations

import logging
from typing import Type

from twister_ext.device.device_abstract import DeviceAbstract
from twister_ext.device.hardware_adapter import HardwareAdapter
from twister_ext.device.qemu_adapter import QemuAdapter
from twister_ext.device.simulator_adapter import (
    CustomSimulatorAdapter,
    NativeSimulatorAdapter,
    UnitSimulatorAdapter,
)
from twister_ext.exceptions import TwisterExtException

logger = logging.getLogger(__name__)


class DeviceFactory:
    _devices: dict[str, Type[DeviceAbstract]] = {}

    @classmethod
    def discover(cls):
        """Return available devices."""

    @classmethod
    def register_device_class(cls, name: str, klass: Type[DeviceAbstract]):
        if name not in cls._devices:
            cls._devices[name] = klass

    @classmethod
    def get_device(cls, name: str) -> Type[DeviceAbstract]:
        logger.debug('Get device type "%s"', name)
        try:
            return cls._devices[name]
        except KeyError as e:
            logger.error('There is no device with name "%s"', name)
            raise TwisterExtException(f'There is no device with name "{name}"') from e


DeviceFactory.register_device_class('custom', CustomSimulatorAdapter)
DeviceFactory.register_device_class('native', NativeSimulatorAdapter)
DeviceFactory.register_device_class('unit', UnitSimulatorAdapter)
DeviceFactory.register_device_class('hardware', HardwareAdapter)
DeviceFactory.register_device_class('qemu', QemuAdapter)
