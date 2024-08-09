<?php
/**
 * Реализовать функцию с тремя параметрами: function mathOperation($arg1, $arg2, $operation),
 * где $arg1, $arg2 – значения аргументов, $operation – строка с названием операции.
 * В зависимости от переданного значения операции выполнить одну из арифметических операций
 * (использовать функции из пункта 3) и вернуть полученное значение (использовать switch).
 */


mathOperation(2, 3, "+");
mathOperation(2, 3, "-");
mathOperation(2, 3, "*");
mathOperation(2, 3, "/");
mathOperation(2, 0, "/");
mathOperation(2, 0, 8);


function mathOperation($arg1, $arg2, $operation)
{
    switch ($operation) {
        case $operation === "+";
            echo $arg1 + $arg2 . PHP_EOL, "<br>";
            break;
        case $operation === "-";
            echo $arg1 - $arg2 . PHP_EOL, "<br>";
            break;
        case $operation === "*";
            echo $arg1 * $arg2 . PHP_EOL, "<br>";
            break;
        case $operation === "/";
            echo ($arg2 != 0) ? $arg1 / $arg2 . PHP_EOL : "делить на ноль нельзя" . PHP_EOL, "<br>";
            break;
        default;
            echo "не корректно введено значения операции", "<br>";
    }
}