
// Create Dictionary
Dictionary<char, int> my_dict = new Dictionary<char, int>();
var romans = new Dictionary<char, int>() {
        ['I'] = 1,
        ['V'] = 5,
        ['X'] = 10,
        ['L'] = 50,
        ['C'] = 100,
        ['D'] = 500,
        ['M'] = 1000
    };

// Create list 
List<string> distinctStrings = new List<string>();
List<string> myList = new List<string>{"Item1", "Item2", "Item3"};
var firstItem = myList[0];

// String builder to access by index 
StringBuilder res = new StringBuilder(your_string);
res[index] = newChar;

// fILTER STRING IsLetterOrDigit
string str = new String(s.ToLower().Where(char.IsLetterOrDigit).ToArray());

// compare strings
bool res = newStr.SequenceEqual(newStr.Reverse());

//  Foreach Dictionary loop
foreach(KeyValuePair<string, string> entry in myDictionary)
{
    // do something with entry.Value or entry.Key
}

foreach (var key in demo.Keys)
{
    Console.WriteLine(key);
    foreach (var elem in demo[key])
    {
        Console.WriteLine(elem);
    }
}

//  Foreach loop
foreach (char we in s){
    if (my_dict.ContainsKey(we)) // Is dict contains Key
    {my_dict[we] += 1;}       // increase key's value
    else{my_dict.Add(we,1); } }    // Add key,value pare to dict 
Console.WriteLine(my_dict.FirstOrDefault(gf => gf.Value == 1).Key);   // look for value and return its key
if (my_dict.ContainsValue(1))                                         // Is dict contains Value
{return my_dict.FirstOrDefault(gf => gf.Value == 1).Key;}             
else{ return '_';}

// For loop
for (int i = 0; i < (values.Count -1); i++){
    Console.WriteLine(i  + values[i]);}  // printing int + string

// Return array of strings of longest strings in array
var longest = inputArray.Where(s => s.Length == inputArray.Max(m => m.Length));
// Return FIRST longest string  from   strings of array 
var longest = inputArray.Where(s => s.Length == inputArray.Max(m => m.Length)).First();
foreach (var item in longest) { Console.WriteLine(item); }

// COvvert int to str
string str = int.ToString();

//  Convert string -> array of strings
string[] result = strings.ToArray();
// Convert array of strings -> list
List<string> values = inputArray.ToList();

// Create empty str, add value , return lenght of str
string er = "";
er += item_s1;
return er.Length;

// Print list of int
foreach(int t in int_list){Console.Write(t);}
int_list.ForEach(p => Console.Write(p));
int_list.ForEach(Console.Write);

// Get range of list values 
Console.WriteLine(int_list.GetRange(0, (str_not_list.Length / 2)));  //GetRange (int index, int count);
