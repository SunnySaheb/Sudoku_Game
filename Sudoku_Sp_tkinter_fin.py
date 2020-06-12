# Simple Sudoku Game in Python using Tkinter
# By Sushobhan Pramanik

from Tkinter import *

from random import randint


def board(canvas, line_distance):
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
      if x % 30 ==0:
         canvas.create_line(x, 0, x, canvas_height, fill="#476042", width=3)
         
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")
      if y % 30 ==0:
         canvas.create_line(0, y, canvas_width, y, fill="#476042", width=3)
       
   canvas.create_rectangle(3, 3, 450, 450, outline='black', width=4)




def createEntry(canvas,arr,color):
   for i in range(1,10,1):
      for j in range(1,10,1):
         p,q=9,9
         E = Entry(canvas, justify="center", font=("Calibri",18), highlightcolor="blue",highlightthickness=1,bd=0, fg=color, width=0)

         E.pack()
         E.insert(0, arr[i-1][j-1])
         E.place(x=(p*i)+(40*(i-1)), y=(p*j)+(40*(j-1)), height=40, width=40)
   


def createButtons(canvas,sol_c,abc,g,h,f,xx):

   button_solve = Button(canvas, text="Solve", command = lambda: sol(arr,sol_c,abc,g,h,f,xx))
   button_solve.pack()
   button_reset = Button(canvas, text="reset", command = lambda: reset(arr))
   button_reset.pack()
   button_solve.place(x=125, y=480, height=30, width=58)
   button_reset.place(x=275, y=480, height=30, width=58)



def sol(arr,sol_c,abc,g,h,f,xx):
   
   l = [0,0]

   if (not find_empty(arr, l,abc,g,h,f,xx)):
      
      print("   --------Solved--------   :)")
                
   else:

      row = l[0]
      col = l[1]

      sol_2(arr, row, col, abc,g,h,f,xx)

               
   print(arr)
   lst = ["red","blue","green"]
   color = lst[randint(0,2)]
   createEntry(canvas,arr,color)



   
def sol_2(arr, row, col,abc,g,h,f,xx):
   
   for ccc in range(9): 
      for vvv in range(9): 
         if(arr[ccc][vvv]== ''): 
            #l[0]= row 
            #l[1]= col 
                   
            for no in range(xx, 10):
                  

               if( check_pos(arr, row, col, no,abc,g,h,f,xx)):

                  arr[row][col] = no

                  abc[g][h] = row
                  g = 1
                  abc[g][h] = col
                  #g += 1
                  #abc[g][h] = no

                  h += 1
                  g = 0
                  
               else:
                  xx = no
                  if no == 9:
                     row = abc[0][h-1]
                     col = abc[1][h-1]
                     xx = 1

                     
               sol_2(arr, row, col,abc,g,h,f,xx)
                  
   return arr          
         



def check_pos(arr, row, col, no,abc,g,h,f,xx):

   return not used_col(arr, row, col, no,abc,g,h,f,xx) and not used_row(arr, row, col, no,abc,g,h,f,xx) and not used_box(arr, row - row % 3, col - col % 3, no,abc,g,h,f,xx)



def used_row(arr, row, col, no,abc,g,h,f,xx): 
   for i in range(9): 
      if(arr[row][i] == no): 
         return True
   return False
   


def used_col(arr, row, col, no,abc,g,h,f,xx): 
   for i in range(9): 
      if(arr[i][col] == no): 
         return True
   return False



def used_box(arr, row, col, no,abc,g,h,f,xx):
   for i in range(3):
      for j in range(3):
         if(arr[row + i][col + j] == no):
            return True
   return False



def find_empty(arr, l,abc,g,h,f,xx):
   for i in range(9):
      for j in range(9):

         if ( arr[i][j] == '' ):
            l[0] = i
            l[1] = j
            return True

   return False




def reset(arr):
   sol_c = 0
   arr = [[ 0 for i in range(9)] for j in range(9)]
   print(arr)
   puzzle(arr)
   print(arr)
   lst = ["red","blue","green"]
   color = lst[randint(0,2)]
   createEntry(canvas,arr,color)
   #color = lst[randint(0,2)]



def check(arr):
   count =  0
   for rw in range(0,9):
      for cl in range(0,9):
         if arr[rw][cl] != '':
            count +=1
            
   if count == 81:
      cnt = 1

      if cnt == 1:
         remove(arr)


def remove(arr):
   for lo in range(9):
      for lk in range(9):

         if arr[lo][lk] != '':

            u = randint(20,40)
            for p in range(u):
               arr[randint(0,8)][randint(0,8)] = ''
            return arr

         else:
            return arr


def pz(arr,rand,i,j):
   square=[]
   if i<3:
     if j<3:
       square=[arr[z][0:3] for z in range(0,3)]
     elif j<6:
       square=[arr[z][3:6] for z in range(0,3)]
     else:  
       square=[arr[z][6:9] for z in range(0,3)]
   elif i<6:
     if j<3:
       square=[arr[z][0:3] for z in range(3,6)]
     elif j<6:
       square=[arr[z][3:6] for z in range(3,6)]
     else:  
       square=[arr[z][6:9] for z in range(3,6)]
   else:
     if j<3:
       square=[arr[z][0:3] for z in range(6,9)]
     elif j<6:
       square=[arr[z][3:6] for z in range(6,9)]
     else:  
       square=[arr[z][6:9] for z in range(6,9)]
   #Check that thzs rand has not already be used on thzs 3x3 square
   if not rand in (square[0] + square[1] + square[2]):
     arr[i][j]=rand
   else:
      rand = randint(1,9)
      pz(arr,rand,i,j)

   check(arr)



def puzzle(arr):

   for x in range(0,81):
      
      i = x // 9
      j = x % 9
      rand = randint(1,9)
      
      if arr[i][j] == 0:

         if not rand in arr[i]:
            
            if not rand in (arr[0][j],arr[1][j],arr[2][j],arr[3][j],arr[4][j],arr[5][j],arr[6][j],arr[7][j],arr[8][j]):
               pz(arr,rand,i,j)

            else:

               while rand in (arr[0][j],arr[1][j],arr[2][j],arr[3][j],arr[4][j],arr[5][j],arr[6][j],arr[7][j],arr[8][j]):
                  rand = randint(1,9)

               pz(arr,rand,i,j)
                   
         else:

            while rand in arr[i]:
               
               rand = randint(1,9)

            if not rand in (arr[0][j],arr[1][j],arr[2][j],arr[3][j],arr[4][j],arr[5][j],arr[6][j],arr[7][j],arr[8][j]):
               pz(arr,rand,i,j)
                  
            else:

               while rand in (arr[0][j],arr[1][j],arr[2][j],arr[3][j],arr[4][j],arr[5][j],arr[6][j],arr[7][j],arr[8][j]):
                  rand = randint(1,9)
               pz(arr,rand,i,j)




if __name__=="__main__":

   canvas = Tk()
   canvas_width = 450
   canvas_height = 450

   cnt = 0
   color = "red"
   sol_c = 0

   abc = [[ 0 for i in range(81)] for j in range(2)]
   #g=h=0
   g=0
   h=0
   f=[ 1 for i in range(81)]
   xx = 1
   
   rs, cs = (9, 9) 
   arr = [[ 0 for i in range(9)] for j in range(9)]
   puzzle(arr)
   
   w = Canvas(canvas, width=canvas_width, height=canvas_height + 78)
   w.pack()

   board(w,50)

   createButtons(canvas,sol_c,abc,g,h,f,xx)

   createEntry(canvas,arr,color)

   mainloop()
