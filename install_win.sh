{
  py -m install colorama
} || {

  echo Trying local install...

  {
    py -m install colorama --user
  } || {
    echo An error ocurred.
  }
}