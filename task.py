def pattern(rows,cols):
  top=" ___ "*(rows)
  middle="/   \\___"*(rows-1)+"/   \\"
  down="\\___/   "*(rows)



  for i in range(rows):
       if i==0:
         print(top)
       print(middle)
       print(down)
rows=int(input("enter the number of rows :"))
columns=int(input("enter the number of coloums :"))
pattern(rows,columns)
