import json
import os

class ReSharp():  # R# Class
    ##
    #
    #
    #
    #
    def Compile(self, filename):
        if filename.endswith(".rsharp"):
            o = open(filename, "r")
            a = o.readlines()
            compiling = True
            print(f"Indexing {filename}...")
            a = open("a.py", "a")
            with open(filename, 'r') as f:
                # Insert Standard Booleans
                var = list()
                # Insert Default Settings
                ioen = False
                reevelibin = False
                base = False
                mlang = False
                for line in f:
                    compileline = line[:-1]
                    if compileline == "keep main":
                        print("Found Keep Main.")
                        a.write("\ndef main()")
                    elif compileline == "modules = package('reeve.rsharp')":
                        reevelibin = True
                        a.write("import reeveforvs.api.PyReeve")
                        print("Getting ReeveLib.rsharp...")
                        os.system("git clone https://github.com/Kai-Builder/reeveforvs.git")

                    elif compileline == "modules = package('io.rsharp')":
                        print("Enabled io.rsharp.")
                        print("WARNING: IO.RSHARP IS OUTDATED. USE REEVE.RSHARP!")
                        ioen = True
                    elif compileline == f"!define":
                        var.extend([var])
                        print("Defined New Macro.")
                    elif compileline == f"writeln":
                        if ioen == False:
                            print("WARNING: Failed To Define 'writeln', Maybe a Missing "
                                  "Package?\n\nIM:GatherError:4992\nIdentifier 'writeln' Undefined.")
                        else:
                            print("Writeln Has Been Called!")
                    elif compileline == "ip":
                        if reevelibin:
                            i = input(">>>")
                        else:
                            print("UNDEFINED FUNCTION 'IP' MISSING FROM REEVE.RSHARP\n\nLNK:938\nIP Is from "
                                  "reeve.rsharp. Try Saying modules = package('io.rsharp') next time")
                    elif compileline == "snippet.Collect { ext.learn.read }":
                        print("Collected Snippet EXT.LEARN.READ + IO WRITE.")
                    elif compileline == "snippet.Collect { def.main as keep main }":
                        print("Def Main As KEEPMAIN (fine)")
                    elif compileline == "join mlang to __CURRENT__ as Rsh":
                        if mlang == True:
                            print("Joined MLANG To Current Script As RSH.")
                        else:
                            print("MLANG\n\nMlang Is a Multilanguage Library Which allows you to change the language "
                                  "through HTML Like Tags.")
                    elif compileline == "index(/basic)":
                        print("Basic has NULL.\nIndex Returned -1")
                    elif compileline == "before:":
                        print("Re;")
                    elif compileline == "use reeve":
                        print("Using Reeve's API.")
                    elif compileline == "using npplintv0.9":
                        print("USING NPP")
                    elif compileline == "powerline -o mp":
                        print("True")
                    elif compileline == "BoolAlpha(io.power.__curr__(statement**), with args * delta)":
                        print("False")
                    elif compileline == "DB.Current({[alphaline**, string& lineof * new] ++inst}) diagram(print " \
                                        "inst**)} new":
                        print("C++")
                    elif compileline == "{":
                        print("beginline")
                    elif compileline == "}":
                        print('endline')
                    elif compileline == "modules = package('reeveforvs')":
                        os.system("git clone reeveforvs")
                    elif compileline == "pv * args w.new(**) while get** --+instance (wtrue * (instance)* ^^new " \
                                        "Table, Meta (String& String True)) with fry as package('fry') build test.dat " \
                                        "arr[random.maxint(arr))]":
                        print("Inserted New PV With New Instance * True Instance Table Meta Valued Instance String "
                              "String As True With FRY (snippet from reeveforvs)")
                    elif compileline == "e\na":
                        print("EEEEE")
                    elif compileline == "global":
                        print("Defined New Global in a.py")
                    elif compileline == "//":
                        print("00")
                    elif compileline == "gg.alkaline--newdef (**) x * statements++ arg**&&getvals** {[(90, var ** x)]}":
                        print("New Table Created.")
                    elif compileline is None:
                        print("ERROR 9\n\nCOMP:176\nError while Parsing, 'newline'.")
        else:
            print(
                f"File Either Does not end With .rsharp Or Has Nothing Inside.\n\nCompiler Error: File, {filename} "
                f"Does not end with .rsharp")
    def Install(self, handlerfile):
        if handlerfile.endswith(".rins"):
            print(f"Installing {handlerfile}...")
            a = open("a.py", "a")
            with open(handlerfile, 'r') as f:
                # Insert Standard Booleans
                var = list()
                # Insert Default Settings
                ioen = False
                reevelibin = False
                base = False
                mlang = False
                for line in f:
                    compileline = line[:-1]
                    o = open(compileline, 'w')
                    o.write('# MODULE! DO NOT WRITE TO.')
                    o.close()

