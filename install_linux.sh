{
  pip3 install colorama
} || {

  echo Trying local install...

  {
    pip3 install colorama --user
  } || {
    echo An error ocurred.
  }
}