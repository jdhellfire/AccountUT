from os import system

system('coverage run AccountUT.py')
system('coverage report -m')
system('coverage html -d LineCov')


system('coverage run --branch AccountUT.py ')
system('coverage report -m')
system('coverage html -d BranchCov')
