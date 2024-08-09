<?php

/**
 * Реализовать основные 4 арифметические операции в виде функции с тремя параметрами – два параметра это числа,
 * третий – операция. Обязательно использовать оператор return.
 */

echo math(2, 3, "+") . PHP_EOL , "<br>";
echo math(2, 3, "-") . PHP_EOL , "<br>";
echo math(2, 3, "*") . PHP_EOL , "<br>";
echo math(2, 3, "/") . PHP_EOL , "<br>";
echo math(2, 0, "/") . PHP_EOL , "<br>";
echo math(2, 0, 8) . PHP_EOL , "<br>";


function math($a, $b, $c)
{
    if ($c === "+") {
        return $a + $b;
    } elseif ($c === "-") {
        return $a - $b;
    } elseif ($c === "*") {
        return $a * $b;
    } elseif ($c === "/") {
        return ($b != 0) ? $a / $b : "делить на ноль нельзя";
    } else
        return "не корректно введено значения операции";
}