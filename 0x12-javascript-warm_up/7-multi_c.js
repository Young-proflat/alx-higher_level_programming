#!/usr/bin/node
const X = isNaN(process.argv[2]);
if (X === true){
  console.log('Missing number of occurences');
} else{
  for (let x = 0; x < X; x++){
    console.log('C is fun')
  }
}
