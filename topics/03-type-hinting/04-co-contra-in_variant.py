import abc

from typing import Generic, TypeVar


class Base:
    def foo(self):
        print("foo")


class Derived(Base):
    def bar(self):
        print("bar")


#################################################################
#################################################################
###################### Covariant Example ########################
#################################################################
#################################################################



T_co = TypeVar('T_co', bound='Base', covariant=True)
# T_co = TypeVar("T_co", bound="Base", contravariant=True)


class Source(Generic[T_co]):
    @abc.abstractmethod
    def generate(self) -> T_co:  # Produce T_co!
        pass


class SourceBase(Source[Base]):
    def generate(self) -> Derived:  # Produce T_co!
        return Derived()


class SourceDerived(Source[Derived]):
    def generate(self) -> Derived:
        return Derived()


source: Source[Base] = SourceDerived()
source.generate()

# Try to uncomment lines below.
# source_derived: Source[Derived] = SourceBase()
# source_derived.generate()


#################################################################
#################################################################
#################### Contravariant Example ######################
#################################################################
#################################################################


T_contra = TypeVar("T_contra", bound="Base", contravariant=True)


class Sink(Generic[T_contra]):
    @abc.abstractmethod
    def consume(self, value: T_contra):
        pass


class SinkBase(Sink[Base]):
    def consume(self, value: Base):
        value.foo()


class SinkDerived(Sink[Derived]):
    def consume(self, value: Derived):
        value.bar()

    def other_func(self):
        pass


base = Base()
derived = Derived()
sink_derived: Sink[Derived] = SinkBase()
# we can safely consumer
# sink_derived.consume(base)
sink_derived.consume(derived)
# Try to uncomment this line.
# sink_derived.other_func()
