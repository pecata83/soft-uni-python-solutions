import java.util.Scanner
import java.util.Stack

public class Pr_07_BalancedParentheses {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in)
        String brackets = sc.nextLine()

        Stack < Character > stack = new Stack <> ()
        // CREATING THE stack FOR THE BRACKETS
        boolean isBalanced = true
        // CHECKING WHETHER THE BRACKETS ARE BALANCED

        for (int i=0
             i < brackets.length()
             i++) {//GETTING THROUGH ALL THE ELEMENTS FROM THE INPUT
                   char bracket = brackets.charAt(i)
                   // GETTING ONE SINGLE BRACKET AND PUTTING IT INTO THE char bracket
                   if (bracket == '{' | | bracket == '[' | | bracket == '(') {//CHECKING WHETHER THE BRACKET TYPE IS THE OPENING ONE
                                                                              stack.push(
                                                                                  bracket)
                                                                              // ADDING THE OPENING BRACKET INTO THE stack
                                                                              } else {
                       if (bracket == '}') {
                           bracket = '{'
                       } else if (bracket == ')') {
                           bracket = '('
                       } else if (bracket == ']') {
                           bracket = '['
                       }

                       if (stack.empty()) {//CHECKING WHETHER THE stack IS EMPTY
                                           isBalanced = false
                                           break
                                           }

                       if (bracket == stack.peek()) {
                           stack.pop()
                       } else {
                           isBalanced = false
                           break
                       }
                   }
                   }

        if (isBalanced) {
            System.out.println("YES")
        } else {
            System.out.println("NO")
        }
    }
}
