# vault-door-training

![image.png](imagesimage.png)

We can see the logic of the code of flag checking. The substring reveals the flag content of `w4rm1ng_Up_w1tH_jAv4_000HPpgh7Ph`

```bash
└─$ cat VaultDoorTraining.java 
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
   }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security                                                                                                                                                               
    // on the other doors.                                                                                                                                                                                                                 
    //                                                                                                                                                                                                                                     
    // -Minion #9567                                                                                                                                                                                                                       
    public boolean checkPassword(String password) {                                                                                                                                                                                        
        return password.equals("w4rm1ng_Up_w1tH_jAv4_000HPpgh7Ph");                                                                                                                                                                        
    }                                                                                                                                                                                                                                      
}                            
```

We can compile the file and test our guess

```bash
└─$ javac VaultDoorTraining.java                                                                                                                                                                                                           
...                                                                                                                                                                                                                                         
└─$ java VaultDoorTraining                                                                                                                                                                                                                 
Enter vault password: picoCTF{w4rm1ng_Up_w1tH_jAv4_000HPpgh7Ph}
Access granted.

```

In fact, you can fill it whatever character for the last character, as it won’t be checked anyways

```bash
└─$ java VaultDoorTraining                                                                                                                                                                                                                 
Enter vault password: picoCTF{w4rm1ng_Up_w1tH_jAv4_000HPpgh7Pha
Access granted.
```

Flag: `picoCTF{w4rm1ng_Up_w1tH_jAv4_000HPpgh7Ph}`
