package testpkg;

public class Permutations
{

  public static int factorial(int num)
  {
    if (num < 0)
    {
      throw new IllegalArgumentException("Negative numbers not currently supported.");
    }
    int product = num;
    for (int i = 1; i < num; ++i)
    {
      product *= num - i;
    }
    return product;
  }

  public void printPermutations(String arg)
  {
    String[] perms = getPermutations(arg);
    for (String perm : perms)
    {
      System.out.println(perm);
    }
  }

  public String[] getPermutations(String arg)
  {
    if (arg == null || arg.length() < 1)
    {
      throw new IllegalArgumentException("Argument must be non-null and at least one character long.");
    }
    String[] permsFound = new String[factorial(arg.length())];
    if (arg.length() == 1)
    {
      permsFound[0] = arg;
    }
    else
    {
      int numPermsFound = 0;
      for (int i = 0; i < arg.length(); ++i)
      {
        String[] subPerms = getPermutations(arg.substring(0, i) + arg.substring(i + 1, arg.length()));
        for (int j = 0; j < subPerms.length; ++j)
        {
          permsFound[numPermsFound++] = arg.charAt(i) + subPerms[j];
        }
      }
    }
    return permsFound;
  }

  public static void main(String[] args)
  {
    String test = "notfre";
    //    int i = 0;
    //    System.out.println(test.substring(0, i));
    //    System.out.println(test.substring(i + 1, test.length()));
    //    System.out.println(factorial(0));
    //    System.out.println(factorial(5));
    //    System.out.println(factorial(-100));
    new Permutations().printPermutations(test);
  }
}
