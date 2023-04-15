# Python Type Hint: Contravariant, Covariant, Invariant

We all know the Liskov substitution principle. The type can be replaced by its subtype without breaking it. But how about the relationship of their generic types, C[subtype] and C[type]?

## So, what is covariant?

If A<: B, you can replace B with A anywhere

We say C[T] where T bound to B is

1. Contravariant, when A <: B => C[A] :> C[B]
We can replace C[B] with C[A] anywhere.

1. Covariant, when A <: B => C[A] <: C[B]

We can replace C[A] with C[B] anywhere. But How to cause this situation?

I will explain in the example code below.

1. Invariant, If both circumstances do not suit. C[A] can not exchange with C[B], and vice versa.

## Combine the concept with Sink / Source

Accordingly to their behaviors, We have two kinds of objects defined.

* Source[T]: It produces T, is covariant to T.
* Sink[T]: It consumes T, is contravariant to T.
