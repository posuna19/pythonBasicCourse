#!/bin/bash

var1="Value of first var"
var2="Value of second var"

echo $0 :: var1 = $var1, var2 = $var2

export  var1
./W1_06_variable_scope2.sh

echo $0 :: var1 = $var1, var2 = $var2
