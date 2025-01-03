from __future__ import annotations

import pytest

from pygerber.gerber.ast.expression_eval_visitor import ExpressionEvalVisitor
from pygerber.gerber.ast.nodes import (
    Add,
    Constant,
    Div,
    Double,
    Expression,
    Mul,
    Parenthesis,
    Sub,
    Variable,
)


def var(name: str) -> Variable:
    return Variable(variable=name)


def const(value: Double) -> Constant:
    return Constant(constant=value)


def add(*operands: Expression) -> Add:
    return Add(head=operands[0], tail=list(operands[1:]))


def sub(*operands: Expression) -> Sub:
    return Sub(head=operands[0], tail=list(operands[1:]))


def mul(*operands: Expression) -> Mul:
    return Mul(head=operands[0], tail=list(operands[1:]))


def div(*operands: Expression) -> Div:
    return Div(head=operands[0], tail=list(operands[1:]))


def parens(inner: Expression) -> Expression:
    return Parenthesis(inner=inner)


@pytest.mark.parametrize(
    ("scope", "expression", "expected"),
    [
        (
            {},
            const(1.0),
            1.0,
        ),
        (
            {"$1": 2.0},
            var("$1"),
            2.0,
        ),
        (
            {},
            add(
                const(1.0),
                const(2.0),
            ),
            3.0,
        ),
        (
            {"$1": 2.0},
            add(
                const(1.0),
                var("$1"),
            ),
            3.0,
        ),
        (
            {"$1": 2.0},
            add(
                var("$1"),
                const(1.0),
            ),
            3.0,
        ),
        (
            {"$1": 2.0, "$2": 1.0},
            add(
                var("$1"),
                var("$2"),
            ),
            3.0,
        ),
        (
            {"$1": 1.66, "$2": 3.0},
            add(
                add(var("$1"), const(5.0)),
                var("$2"),
            ),
            1.66 + 3.0 + 5.0,
        ),
        (
            {"$1": 1.66, "$2": 3.0},
            add(
                var("$2"),
                add(var("$1"), const(5.0)),
            ),
            1.66 + 3.0 + 5.0,
        ),
        (
            {"$1": 1.66, "$2": 3.0},
            add(
                var("$1"),
                sub(var("$2"), const(5.0)),
            ),
            1.66 + (3.0 - 5.0),
        ),
        (
            {"$2": 3.0},
            sub(
                var("$2"),
                sub(const(1.66), const(5.0)),
            ),
            3.0 - (1.66 - 5.0),
        ),
        (
            {"$1": 3.0, "$2": 5.0},
            mul(
                var("$1"),
                sub(const(1.66), var("$2")),
            ),
            3.0 * (1.66 - 5.0),
        ),
        (
            {"$1": 3.0, "$2": 5.0},
            div(
                var("$1"),
                var("$2"),
            ),
            3.0 / 5.0,
        ),
        (
            {"$1": 3.0, "$2": 5.0},
            add(
                div(const(1.66), var("$1")),
                var("$2"),
            ),
            (1.66 / 3.0) + 5.0,
        ),
        (
            {"$1": 3.0, "$2": 5.0},
            mul(
                div(const(1.66), var("$1")),
                var("$2"),
            ),
            (1.66 / 3.0) * 5.0,
        ),
        (
            {"$1": 3.0, "$2": 5.0},
            div(
                mul(const(1.66), var("$1")),
                var("$2"),
            ),
            (1.66 * 3.0) / 5.0,
        ),
        (
            {"$1": 3.0, "$2": 5.0},
            div(
                var("$2"),
                mul(const(1.66), var("$1")),
            ),
            5.0 / (1.66 * 3.0),
        ),
        (
            {"$1": 3.0, "$2": 5.0},
            div(
                var("$2"),
                parens(mul(const(1.66), var("$1"))),
            ),
            5.0 / (1.66 * 3.0),
        ),
    ],
    ids=[
        "00_[const]",
        "01_[var]",
        "02_[const+const]",
        "03_[const+var]",
        "04_[var+const]",
        "05_[var+var]",
        "06_[[var+const]+var]",
        "07_[var+[var+const]]",
        "08_[var+[var-const]]",
        "09_[var-[const-const]]",
        "10_[var*[const-var]]",
        "11_[var/var]",
        "12_[[const/var]+var]",
        "13_[[const/var]*var]",
        "14_[[const*var]/var]",
        "15_[var/[const*var]]",
        "16_[var/parens([const*var])]",
    ],
)
def test_expression_eval(
    scope: dict[str, Double], expression: Expression, expected: Double
) -> None:
    visitor = ExpressionEvalVisitor(scope)
    assert visitor.evaluate(expression) == expected
