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
{ // Beginning Line (beginline)
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

# End 1
Thank you for trying R#.