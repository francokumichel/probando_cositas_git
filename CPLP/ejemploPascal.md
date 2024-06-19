```pascal
program Hello;
type 
    v = array[1..10] of integer;
    
procedure procedimiento(var arraysito: v);
var 
b: v;
begin
    writeln(arraysito[1]);
    arraysito[1]:= 5000;
    writeln(arraysito[1]);
    b[1]:= 13;
    b[2]:= 23;
    arraysito:= b; 
end;

var a: v; b: v; aux: v;
begin

  a[1]:= 10;
  a[2]:= 100;
  procedimiento(a);
  writeln(a[1],' ',a[2]);

end.
```