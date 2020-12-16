import xlsxFile from 'read-excel-file'

const xlsxFile = require('read-excel-file/node');
 
 xlsxFile('./infant-hat.xlsx').then((rows) => {
  console.log(rows);
  console.table(rows);
 })
 
