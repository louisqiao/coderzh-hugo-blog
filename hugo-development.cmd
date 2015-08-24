@echo off 
rd /S /Q public
md public

myhugo server -w -v
