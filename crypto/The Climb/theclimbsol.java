import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
public class Main
{
    int size;
    int kmatrix[][];
    int ciphermatrix[];
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
 
    public void perf(String cipher)
    {
        cipherconv(cipher);
        multiply(cipher.length());
        res(cipher.length());
    }
 
    public void keyconv(String key, int len)
    {
        kmatrix = new int[len][len];
        int a = 0;
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                kmatrix[i][j] = ((int) key.charAt(a)) - 97;
                a++;
            }
        }
    }
 
    public void cipherconv(String cipher)
    {
        ciphermatrix = new int[cipher.length()];
        for (int i = 0; i < cipher.length(); i++)
        {
            ciphermatrix[i] = ((int) cipher.charAt(i)) - 97;
        }
    }
 
    public void multiply(int len)
    {
        rmatrix = new int[len];
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                rmatrix[i] += kmatrix[i][j] * ciphermatrix[j];
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
 
    public void cofactor(int mat[][], int size)
    {
        int c[][], fact[][];
        c = new int[size][size];
        fact= new int[size][size];
        int p, q, m, n, i, j;
        for (q = 0; q < size; q++)
        {
            for (p = 0; p < size; p++)
            {
                m = 0;
                n = 0;
                for (i = 0; i < size; i++)
                {
                    for (j = 0; j < size; j++)
                    {
                        c[i][j] = 0;
                        if (i != q && j != p)
                        {
                            c[m][n] = mat[i][j];
                            if (n < (size - 2))
                                n++;
                            else
                            {
                                n = 0;
                                m++;
                            }
                        }
                    }
                }
                fact[q][p] = (int) Math.pow(-1, q + p) * det(c, size - 1);
            }
        }
        transp(fact, size);
    }
    
     public int det(int a[][], int n)
    {
        int result;
        if (n == 1)
            result = a[0][0];
        else if (n == 2)
        {
            result = a[0][0] * a[1][1] - a[1][0] * a[0][1];
        }
        else
        {
            result = 0;
            for (int j1 = 0; j1 < n; j1++)
            {
                int m[][] = new int[n - 1][n - 1];
                for (int i = 1; i < n; i++)
                {
                    int j2 = 0;
                    for (int j = 0; j < n; j++)
                    {
                        if (j == j1)
                            continue;
                        m[i - 1][j2] = a[i][j];
                        j2++;
                    }
                }
                result += Math.pow(-1.0, 1.0 + j1 + 1.0) * a[0][j1]
                        * det(m, n - 1);
            }
        }
        return result;
    }
 
    void transp(int fact[][], int r)
    {
        int i, j;
        int b[][], inverse[][];
        b = new int[r][r];
        inverse = new int[r][r];
        int d = det(kmatrix, r);
        int mi = mi(d % 26);
        mi %= 26;
        if (mi < 0)
            mi += 26;
        for (i = 0; i < r; i++)
        {
            for (j = 0; j < r; j++)
            {
                b[i][j] = fact[j][i];
            }
        }
        for (i = 0; i < r; i++)
        {
            for (j = 0; j < r; j++)
            {
                inverse[i][j] = b[i][j] % 26;
                if (inverse[i][j] < 0)
                    inverse[i][j] += 26;
                inverse[i][j] *= mi;
                inverse[i][j] %= 26;
            }
        }
        matrixtoinvkey(inverse, r);
    }
 
    public int mi(int d)
    {
        int q, r1, r2, r, t1, t2, t;
        r1 = 26;
        r2 = d;
        t1 = 0;
        t2 = 1;
        while (r1 != 1 && r2 != 0)
        {
            q = r1 / r2;
            r = r1 % r2;
            t = t1 - (t2 * q);
            r1 = r2;
            r2 = r;
            t1 = t2;
            t2 = t;
        }
        return (t1 + t2);
    }
 
    public void matrixtoinvkey(int inv[][], int n)
    {
        String invkey = "";
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                invkey += (char) (inv[i][j] + 97);
            }
        }
        keyconv(invkey, size);
    }
 
    public static void main(String args[]) throws IOException
    {
        Main obj = new Main();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the ciphertext: ");
        String cipher = in.readLine();
        System.out.println("Enter the key: ");
        String key = in.readLine();
        double root = Math.sqrt(key.length());
        if (root != (long) root)
            System.out.println("Invalid key length.");
        else
        {
            int s = (int) root;
            obj.size = s;
                System.out.println("Result:");
                obj.keyconv(key, s);
                obj.cofactor(obj.kmatrix, s);
                obj.div(cipher, s);
        }        
    }
}