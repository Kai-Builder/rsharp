import json
import os


class ReSharp:  # R# Class
    ##
    #
    #
    #
    #
    @staticmethod
    def Compile(filename):
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
                alk = False
                for line in f:
                    compileline = line[:-1]
                    if compileline == "keep main":
                        print("Found Keep Main.")
                        a.write("\ndef main()")
                    elif compileline == "include module alkaline":
                        print("Gathering Alkaline..")
                        print("Found Alkaline!")
                        alk = True
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
                        if ioen:
                            i = input(">>>")
                        else:
                            print("UNDEFINED FUNCTION 'IP' MISSING FROM REEVE.RSHARP\n\nLNK:938\nIP Is from "
                                  "reeve.rsharp. Try Saying modules = package('io.rsharp') next time")
                    elif compileline == "snippet.Collect { ext.learn.read }":
                        print("Collected Snippet EXT.LEARN.READ + IO WRITE.")
                    elif compileline == "after:":
                        print("Be;")
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
                    elif compileline == "alkaline.BoolAlpha(io.power.__curr__(statement**), with args * delta)":
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
                        if alk == True:
                            print("New Table Created.")
                        else:
                            print("Error, Library: 'gg' Not Detected.")
                    elif compileline == "gg.alkaline--uproc++ str** string& {{Operator**}} Get& Values[2]":
                        if alk:
                            print("Alkaline Values two")
                        else:
                            print("Error, Library: 'gg' Not Detected.")
                    elif compileline == "install {LIB.RSH.ALL}":
                        print("Installing All Base Modules...")
                    elif compileline == "stretch main[argv**, new++]":
                        print("Stretched Main With ARGV, And NEW++")
                    elif compileline == "<diff>":
                        print("1010192010")
                    elif compileline == "<undiff>":
                        print("9001080299")
                    elif compileline == "<udif lang=='rsharp'>":
                        print("RSHARP LANGUAGE")
                    elif compileline == "\n":
                        print("ERROR 9\n\nCOMP:176\nError while Parsing, 'newline'.")
                    elif compileline == "callback(malloc)":
                        print("Error. Cannot Concatenate System Variable, 'malloc'")
                    elif compileline == "index(/basic/standard/functions_base)":
                        print("INDEXED basic/standard/functions_base, Got 93087 Results.")
                    elif compileline == "print('indexp_(getcr**, functions)'":
                        print("Table Of functions_base")
                        print("SystemFunction 187KB")
                        print("DataTable 19MB")
                        print("meta Tables 19281783276KB")
                    elif compileline == "require module r_dynamics":
                        print("Required R DYNAMICS")
                        p = open("Hl.rnamic", "w")
                        p.close()
                    elif compileline == "R DYNAMIC INIT":
                        print("On Line __line__, initialized R Dynamics")
                    elif compileline == "dynamics++ [[--++namics]] properties{DYNAIMCS.NAME = newdynamic, " \
                                        "DYNAMICS.WRITE = newdynamic}":
                        print("GGNAMICS")
        else:
            print(
                f"File Either Does not end With .rsharp Or Has Nothing Inside.\n\nCompiler Error: File, {filename} "
                f"Does not end with .rsharp")

    def Install(self, handlerfile):
        if handlerfile.endswith(".rins"):
            print(f"Installing {handlerfile}...")
            a = open("a.py", "a")
            with open(handlerfile, 'r') as f:
                for line in f:
                    compileline = line[:-1]
                    o = open(compileline, 'w')
                    o.write('# MODULE! DO NOT WRITE TO.')
                    o.close()
