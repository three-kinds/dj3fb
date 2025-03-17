# -*- coding: utf-8 -*-
import abc
from typing import Tuple, Optional
from django.db import models
from django.contrib.postgres import fields as pg_fields


class BaseFieldTemplate(abc.ABC):
    f_lib = "from dj3fb.faker_utils import f"

    def __init__(self, field: models.Field):
        self.field = field

    @abc.abstractmethod
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_list_item_expression(self) -> str:
        raise NotImplementedError()


class SmallIntegerFieldTemplate(BaseFieldTemplate):
    delta = 0

    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        if self.field.choices is not None:
            choices = [k for k, _ in self.field.choices]
            return None, f"factory.Iterator({str(choices)})"
        else:
            return None, f"factory.Sequence(lambda n: n + {self.delta})"

    def get_list_item_expression(self) -> str:
        if self.field.choices is not None:
            choices = [k for k, _ in self.field.choices]
            return f"random.choice({str(choices)})"
        else:
            return f"n + m + {self.delta}"


class IntegerFieldTemplate(SmallIntegerFieldTemplate):
    delta = 10000


class BigIntegerFieldTemplate(SmallIntegerFieldTemplate):
    delta = 100000000


class BinaryFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return "memoryview(f.binary(1024))"


class BooleanFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return "f.boolean()"


class CharFieldTemplate(BaseFieldTemplate):
    field: models.CharField

    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        if self.field.choices is not None:
            choices = [k for k, _ in self.field.choices]
            return None, f"factory.Iterator({str(choices)})"
        else:
            return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        if self.field.choices is not None:
            choices = [k for k, _ in self.field.choices]
            return f"random.choice({str(choices)})"
        else:
            return f"f.pystr(max_chars={self.field.max_length or 32})"


class DateFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return "f.date_this_century()"


class DateTimeFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return "f.date_time_this_century()"


class DecimalFieldTemplate(BaseFieldTemplate):
    field: models.DecimalField

    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        left_digits = None
        if self.field.max_digits is not None and self.field.decimal_places is not None:
            left_digits = self.field.max_digits - self.field.decimal_places
        return f"f.pydecimal(left_digits={left_digits}, right_digits={self.field.decimal_places})"


class DurationFieldTemplate(BaseFieldTemplate):
    field: models.DurationField

    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return "f.time_delta()"


class EmailFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return "f.email()"


class FilePathFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return "f.file_path()"


class FileFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return None, "factory.django.FileField()"

    def get_list_item_expression(self) -> str:
        raise AssertionError("FileField is not supported")


class FloatFieldTemplate(BaseFieldTemplate):
    field: models.FloatField

    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return f"f.pyfloat()"


class GenericIPAddressFieldTemplate(BaseFieldTemplate):
    field: models.GenericIPAddressField

    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        if self.field.protocol == "ipv6":
            s = "f.ipv4()"
        else:
            s = "f.ipv6()"
        return s


class ImageFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return None, f"factory.django.ImageField()"

    def get_list_item_expression(self) -> str:
        raise AssertionError("ImageField is not supported")


class JSONFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return f"f.json()"


class TextFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return f"f.text()"


class TimeFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return f"f.time()"


class URLFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return f"f.url()"


class UUIDFieldTemplate(BaseFieldTemplate):
    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda _: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        return f"f.uuid4()"


# pg_fields

class ArrayFieldTemplate(BaseFieldTemplate):
    field: pg_fields.ArrayField

    def __init__(self, field: models.Field, base_field_template: BaseFieldTemplate):
        super().__init__(field)
        self.base_field_template = base_field_template

    def get_fake_expression(self) -> Tuple[Optional[str], str]:
        return self.f_lib, f"factory.Sequence(lambda n: {self.get_list_item_expression()})"

    def get_list_item_expression(self) -> str:
        if self.field.size is not None:
            size = self.field.size
        else:
            size = 3

        return f"[{self.base_field_template.get_list_item_expression()} for m in range({size})]"
