public class Main
{
    int kmatrix[][];
    int tmatrix[];
    int rmatrix[];
 
    public void div(String temp, int size)
    {
        while (temp.length() > size)
        {
            String substr = temp.substring(0, size);
            temp = temp.substring(size, temp.length());
            perf(substr);
        }
        if (temp.length() == size)
            perf(temp);
        else if (temp.length() < size)
        {
            for (int i = temp.length(); i < size; i++)
                temp = temp + 'x';
            perf(temp);
        }
    }
 
    public void perf(String text)
    {
        textconv(text);
        multiply(text.length());
        res(text.length());
    }
 
    public void keyconv(String key, int len)
    {
        kmatrix = new int[len][len];
        int c = 0;
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                kmatrix[i][j] = ((int) key.charAt(c)) - 97;
                c++;
            }
        }
    }
 
    public void textconv(String text)
    {
        tmatrix = new int[text.length()];
        for (int i = 0; i < text.length(); i++)
        {
            tmatrix[i] = ((int) text.charAt(i)) - 97;
        }
    }
 
    public void multiply(int len)
    {
        rmatrix = new int[len];
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                rmatrix[i] += kmatrix[i][j] * tmatrix[j];
            }
            rmatrix[i] %= 26;
        }
    }
 
    public void res(int len)
    {
        String res = "";
        for (int i = 0; i < len; i++)
        {
            res += (char) (rmatrix[i] + 97);
        }
        System.out.print(res);
    }
 
 
    public static void main(String[] args)
    {
        Main obj = new Main();
        System.out.println("Enter the plain text: ");
        String text = "fakeflag";
        System.out.println(text);
        System.out.println("Enter the key: ");
        String key = "gybnqkurp";
        System.out.println(key);
        double root = Math.sqrt(key.length());
        if (root != (long) root)
            System.out.println("Invalid key length.");
        else
        {
            int size = (int) root;
               
                System.out.println("Encrypted text = ");
                obj.keyconv(key, size);
                obj.div(text, size);
        }
    }
}