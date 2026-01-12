#!/bin/bash

for i in {1..50};
do
    curl http://wily-courier.picoctf.net:xxxxx/check -b "name=$i"
done
