<?php

/**
 * Объявить массив, индексами которого являются буквы русского языка,
 * а значениями – соответствующие латинские буквосочетания
 * (‘а’=> ’a’, ‘б’ => ‘b’, ‘в’ => ‘v’, ‘г’ => ‘g’, …, ‘э’ => ‘e’, ‘ю’ => ‘yu’, ‘я’ => ‘ya’).
 * Написать функцию транслитерации строк.
 */

$string = "Тестовая строка, домашня работа, задача 4";
echo $string . "\n" . "<br>";


$alphabet = [
    'а' => 'a', 'б' => 'b', 'в' => 'v',
    'г' => 'g', 'д' => 'd', 'е' => 'e',
    'ё' => 'e', 'ж' => 'zh', 'з' => 'z',
    'и' => 'i', 'й' => 'y', 'к' => 'k',
    'л' => 'l', 'м' => 'm', 'н' => 'n',
    'о' => 'o', 'п' => 'p', 'р' => 'r',
    'с' => 's', 'т' => 't', 'у' => 'u',
    'ф' => 'f', 'х' => 'h', 'ц' => 'c',
    'ч' => 'ch', 'ш' => 'sh', 'щ' => 'sch',
    'ь' => '\'', 'ы' => 'y', 'ъ' => '\'',
    'э' => 'e', 'ю' => 'yu', 'я' => 'ya'
];

function translate($string, $alphabet)
{
    $result = "";
    for ($i = 0; $i < mb_strlen($string); $i++) {
        $letter = mb_substr($string, $i, 1);

        if (isset($alphabet[mb_strtolower($letter)])) {
            if ($letter === mb_strtolower($letter)) {
                $latin_letter = $alphabet[$letter];
            } else {
                $latin_letter = ucfirst($alphabet[mb_strtolower($letter)]);
            }
        } else {
            $latin_letter = $letter;
        }
        $result .= $latin_letter;

    }
    return $result;
}

    echo translate($string, $alphabet);
