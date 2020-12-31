![Build|Data](https://img.shields.io/jetbrains/plugin/v/9630)


# R# Compiler. The All-in-one Debugger, Compiler, And Inspection. In one script.
The R# Compiler is a Python Debugger And Compiler For R#. 
The Compiler Features Many New ways to use Reeve.

# Do's And Don'ts

When using the Reeve Compiler, For the best experience Follow these Rules.

- When Programming In R#, R# Accepts every function with a NEWLINE Function.
  
    - Example
```
snippet.Collect { ext.learn.read } // INCORRECT!
  ```
```
snippet.Collect { ext.learn.read }
// NewLine. Correct!
```
- When Using the snippet Function, It's always recommended to Use A Class Inside to Store Something Compiled as a **"Cell"**. See The Cell Section
For More Information.
```
snippet.Collect { ext.learn.read } // EXT Is a Sample Class Made By Kai-Builder For External Keeping. Awesome!
```
```
snippet.Collect { read() } // Would Work the same, Has no sample class so can not be called anywhere else.
```
- Make sure to always use `modules = package("")` Instead Of Any other variable instance because that is what the compiler understands.


- ALWAYS PUT keep main AT THE START OF YOUR SCRIPTS! IT IS THE MAIN GATHERER.


- When using `!define` Do NOT Put anything else at the end. This Requires Post-Editing Before use.


- The Compiler is Equal TO A  Generator. Use it As one.


- The `before` Function Awaits a certain Function To be true until Use.
```
keep main // Keep Main As MAIN

snippet.Collect { def.main as keep main } // keeps MAIN as keep main

before // Await JOIN To MLANG (www.reeveapi.ga/rsharp/mlang.html)

join mlang to __CURRENT__ as Rsh // Join MultiLanguageLib To Current As Defined As RSH.
```

- Reeve Is a One-Line Like language Meaning it's mostly words.


- R# Contains something Called a BOXER. A Boxer Holds a statement for a certain time frame.
```c++
keep main

BoolAlpha(io.power.__curr__(statement**), with args * delta) // Returns TRUE since BoolAlpha Prints bool.
/*
  IO.Power is a subclass which contains __curr__ That prints if the power is currently enabled. Would return true.
  Io is a class which has functions used for Input Output Streams.
  with args and delta is a simple function which returns bool value with delta rules. Scroll down for all Subclass help.
*/

////// BOXER DEFINITION \\\\\\\\
{ // Beginning Line (beginline)````
DB.Current({[alphaline**, string& lineof * new] ++inst}) diagram(print inst**)} new
} // End Line (endline)
```

- R# Is Basically A List of snippets Inside its own standalone Packaging.


- R# Code Can Be Very Confusing, That's why there's some specific Snippet-Code like One-Line Type Snippets which ease Development
```
keep main

BoolAlpha(io.power.__curr__(statement**), with args * delta)

{
DB.Current({[alphaline**, string& lineof * new] ++inst}) diagram(print inst**)} new
pv * args w.new(**) while get** --+instance (wtrue * (instance)* ^^new Table, Meta (String& String True)) with fry as package('fry') build test.dat arr[random.maxint(arr))]
}
```

- R# Is very specific. Meaning there's no Big Customization Except for when a.py Gets Built.


# Delta Rules (* delta *)
Delta Is a Function Usually Called inside R# Class snippets. It Is usually Displayed in BoolAlpha OR DB Statements.

Delta Rules is just the boundary your Delta Can capture.
The Delta depends on what time your computer clocks it at, it takes it, and recycles it until the Delta is even. Then it has a >1 * 0 + 1% Tick rate every second.

Delta is a Keyword Argument Which prints Current Data Of time on your Computer/Phone.

When Printing, It does not use the Buffering Stream which allows R# TO be PreCompiled After Python is.
R# Runs on Python With syntax. But has the ability To utilize Its own Debugging thread which can be customized.

After Printing Time, It Recycles the Time So it could refresh the Buffering Rate to Cycle it with the CYCLON Module.

```
BoolAlpha(io.power.__curr__(statement**), with args * delta)
```
Delta Is Multiplied For A Correct and accurate Result Most of the time.

# The ** Statement.
** Stands for Cache,  And the Compiler Caches this Symbol Until.. Infinity.
The reason I Implemented this function was to test out the Recalling functions from different statements without redefinition.

The ** Allows For Global Definition Anywhere Regardless of position.
This Symbol Is Essentially the `GLOBAL` Keyword (More info in keywords)

The ** Statement is also used to Define the 2x Multiplication Of a Variable, Not only that, But it can also do as shown below.

```
// This is a ALKALINE Statement. The arg And getvals Will be used elsewhere. That's why we call ** as a Increment
//                                             This is Where i use it as a Mathmatical Operand.
gg.alkaline--newdef (**) x * statements++ arg**&&getvals** {[(90, var ** x)]}
```

# // "The Comment"
The Comment Block "//" Is ONLY TO BE USED IN EMPTY SPACE!
The compiler will sense it as a Cancellation Operator Which cancels a statement.
```
DB.Current({[alphaline**, string& lineof * new] ++inst}) diagram(print inst**)} new
pv * args w.new(**) while get** --+instance (wtrue * (instance)* ^^new Table, Meta (String& String True)) with fry as package('fry') build test.dat arr[random.maxint(arr))] 
// Comments Are Permitted Here!
```
```
DB.Current({[alphaline**, string& lineof * new] ++inst}) diagram(print inst**)} new // But Not Here...
pv * args w.new(**) while get** --+instance (wtrue * (instance)* ^^new Table, Meta (String& String True)) with fry as package('fry') build test.dat arr[random.maxint(arr))] 

```
The Comment Is used to Document Code and is very Good for Documentation.

**The Comment.**


**Params: characters**


**Returns: 00**

# The {{ Statement.
{{ is Used as a Declarator OR A Equation Holder As Shown.
```
// This is a alkaline NewDef Function. As you can see at the End I Used {[()]} as a Equation Holder.
gg.alkaline--newdef (**) x * statements++ arg**&&getvals** {[(90, var ** x)]}
```
It is Used In Comparison with BOXERS For Easy manip.

# The stretch Statement
The Stretch Statement Allows The **MAIN** To be Stretched Until NULL.
```
stretch main[argv**, new++]
```
Scripts Like the one shown below give a good example on how the compiler handles the Scripts.
```cpp
keep main
stretch main[argv**, new++]
include module alkaline
use reeve

modules = package('io.rsharp')
{
ip
// IP Is a Function Which allows User input.
!define
!define
index(/basic)
gg.alkaline--uproc++ str** string& {{Operator**}} Get& Values[2]
// Module Alkaline
}
// Closed Line
// BEFORE: Allows functions inside to be passed anywhere!
before:
join mlang to __CURRENT__ as Rsh
using npplintv0.9

after:
powerline -o mp
```

# Before: And After: Statements
The Before and after statements allow code under them to be executed first or last dependent on where your code is.

As you could see, The Before Function Joins MLANG To The Current Script.
```buildoutcfg
before:
join mlang to __CURRENT__ as Rsh
using npplintv0.9
```
The AFTER Statement takes effect After and is always put at the END.

# Editor Config
The In-Script Compiler Allows you to customize your Install Builds for your dependencies.

Every Install List Is Opened Like so.
```

compiler.ReSharp.Install(0, 'lists.rins')

```
This Function will Install the .rins List which stands for Reeve Installer File.

# Why Python And Not C++?
I've Made a couple of Binary Releases For C++, I Felt python would be easier for others than C++ Would Since Python is a Pre-Compiled Language. Makes Sense?

# MLANG
MLANG is a multilanguage switcher Lib Which works With HTML-Type Tags.
EXAMPLE!
```cpp
before:
{
<diff>
// This is written in C++ LOL

int main() {
    std::cout << "I'm Writing this in RSharp. LOL!";
}

<undiff>
}
```
MLANG is simple and very powerful if used correctly.

# The Index() Feature.
`Index({library})` Is a Targeted Function Which allows Users to Index Certain Library Functions Throughout the R# SESSION LIBRARY HOLDER, Or, The Cloud.

1.3 At minimum Features new ways to index the Libraries.
Here's Some Examples!

```
keep main
print('indexp_(getcr**, functions)
snippet.Collect { def.main as keep main }
dynamics++ [[--++namics]] properties{DYNAIMCS.NAME = newdynamic, DYNAMICS.WRITE = newdynamic}
{
index(/basic/standard/functions_base)
// Indexes basic/std/functions_base Library
}
// Index Function-Base
```
The Index Function Will Index Functions and Look for All.

# Print VS writeln
Print is a formatted Edit of writeln with Text Decoration As Shown Below.

```
print('indexp_(getcr**, functions')
```
PRINT Must have a Variable inside. if not, It will arise a PrintError.
Use writeln For Basic IO Format.

# snippet.Collect { abc }
Snippet.Collect is a Flavorful Function Made to ease Development by inserting pre-defined snippets, with no extra install needed.

Go to the Snippet System Category To Learn how they work
# CHANGELOG
RSharp 1.3 Adds Loads new Features.

The Features have already been Documented As shown above. (and BELOW)

# The Snippet System

Snippet Collector Collects Code Snippets and Binary Formats.

The Kword, `snippet.Collect { def.main as keep main }`, Collects Many Different Edits Of keep main, That's how you enable the STRETCH keyword for main.

EXAMPLE VV

```
keep main // << CANCELLATION OPERATOR, IT FINDS KEEP MAIN BUT CANCELS IT OUT
snippet.Collect { def.main as keep main }
stretch main[argv**, new++]
```

The Snippets are Temporary and can be used anywhere.

# CallBack 

The Callback Function Concatenates 3 Things.

- Type

- Data

- Value
 
The Callback Function Prints Out Certain Vars, And Like other functions, this one is Targeted Meaning it can only be read from the compiler by the RULEBOOK, or [This](keysharp/data/__init__.py).

# Targeted VS Static VS Dynamic Functionality
The Targeted Functions Are In the scope of the __init__.py Document and Can only be changed with the compiler. These are the Basic Functions that are written to a File Called a.py. 
Targeted Functions Use the init python File For Functionality and are written and read by the cp.

Statics Are KWORDS ONLY.
Kword Stands for Keyword and Are only available in the **SourceForge Binary C Release.**
The Statics Are Just Keywords With their own defs.

Dynamic Functionality Is Also ONLY available in the SourceForge Binary C Release. These are the `Array` Types, `strings`, `literals`, `classes`, And More.
# Linkers
The Linker, Or (LNK) As Mentioned in the Compiler's script, Links The Compiler And File together, it opens it, Reads, And Makes a new file which then translates R# To .PY
The Linker Is a Simple tool and it comes out-of-the-box with The R# Compiler.

The LNK Uses Python To Open .rsharp Files and read them.
# Abbreviations
### LNK
LNK Stands for the Standard Linker used to compile .rsharp Files.
### IMP
The IMP Stands for Import, This abbreviation would show if you imported a Package which wasn't signed. (UPDATED IN 1.3)
### DB or STD
- DB
  - The DB is a Library made for Functions that ease the Production of functions like Delta.
- STD
  - We all know this one, STD, STANDARD LIBRARY. This Class Contains Functions which can be used for R#. Comes with reeve.rsharp.
  

# Developer Sheet
If you'd Like to try the Dev Sheet to become an active worker On R#, Or you have something I Don't/Can't Do, DM Me on Discord, Or Submit a Form As a Issue.

