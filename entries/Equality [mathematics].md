<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

Equality, usually denoted with "=" (the equals sign), is used in almost all fields of mathematics as a way to express that two variables or objects refer to the same thing. Because of its more open definition, its not uncommon for some fields to redefine equality in a more rigorous way. Some examples of this are:

- [Set Theory](Set Theory [mathematics]): for sets \\(A\\) and \\(B\\), \\(A = B\\) is defined as \\( \forall x\ldotp (x \in A \leftrightarrow x \in B) \\).

- [Category Theory](Category Theory [mathematics]): assuming \\( f: X \to Y \\) and \\(g: X \to Y\\), then \\(f = g\\) means \\( \forall x \in X\ldotp \left(f(x) \in Y \to f(x) = g(x) \right)\\).

### Properties

Usually, when defining equality on a set \\(S\\) its properties are:

- Reflexive: \\(\forall a \in S\ldotp a = a\\)
- Symmetric: \\(\forall a \in S\ldotp\forall b \in S\ldotp (a = b \to b = a)\\)
- Transitive: \\(\forall a \in S\ldotp\forall b \in S\ldotp\forall c \in S\ldotp (a = b \text{ and } b = c \to a = c)\\)
- Substituitive: assuming \\(F: S \to R\\), then \\(\forall a \in S\ldotp\forall b \in S\ldotp F(a) = F(b)\\)
- Antisymmetric: \\(\forall a \in S\forall b \in S\ldotp (a = b \text{ and } b = a \to a = b)\\)

Equality is the most basic of symmetric [partial orders](Partial Order [mathematics]) in that most of these orders are built some kind of equality baked in the relation.

## Computer Science

Sometimes, in [computer science](Computer Science), equality (also seen as "==") may not have some of the propeties above (some [languages](Programming Languages [computing]) call this *partial equality*). The most common of these cases happens in [floating point](Floating Point [computing]) arithmetic, where there is an object <tt>NaN</tt>, called *not a number*. For this object, reflexivity does not holds, thus \\( \text{NaN} \ne \text{NaN}\\). In the case of a variable <tt>x</tt> that is defined as <tt>NaN</tt> or became a <tt>NaN</tt> as a result of some operation, then <tt>x == x</tt> is false, which can lead to some unexpected behaviour.

Because of the different ways equality can be expressed, some languages define more than one equality operation. In [SWI-Prolog](Prolog [programming language]) for example, there is unification ("=") which can be used for some kinds of comparison, there is also term equality ("==") and arithmetic equality ("=:="). Another languages, like [Python](Python) also defines an identity equality, that is true only when elements are the same resource-wise, in which case the properties discussed above are held.