<?php

/**
 * Написать функцию, которая вычисляет текущее время и возвращает его в формате с правильными склонениями, например:
 * 22 часа 15 минут
 * 21 час 43 минуты.
 */


function timeDeclination($number, $word1, $word2, $word3)
{
    {
        if ($number > 10 && $number <= 20) return $word1;
        else {
            return match ($number % 10) {
                1 => $word2,
                2, 3, 4 => $word3,
                default => $word1,
            };
        }

    }
}

echo "22 " . timeDeclination(22, "часов", "час", "часа") . " 15 " . timeDeclination(15, "минут", "минута", "минуты") . "\n";
echo "21 " . timeDeclination(21, "часов", "час", "часа") . " 43 " . timeDeclination(43, "минут", "минута", "минуты") . "\n";

