def pattern(rows,cols):
  top=" ___ "*(cols)
  middle="/   \\_"*(cols-1)+"/   \\"
  down="\\_/   "*(cols)
  top1=" _   "



  for i in range(rows):
       if i==0:
         print(top)
       print(middle)
       print(down)
rows=int(input("enter the number of rows :"))
columns=int(input("enter the number of coloums :"))
pattern(rows,columns)
