
# Made by: Joona Nykänen
# Date: 28.01.2023

SCHEME_DELIM = "://"
PATH_DELIM = "?"
PARAM_DELIM = "&"
ENTRY_DELIM = "="
VALID_SCHEME = "visma-identity"
VALID_PATHS = ["login", "confirm", "sign"]
VALID_PARAMS = ["source", "paymentnumber", "documentid"]


class Identificator:
    def __init__(self, URI: str):
        try:
            self.path = ""
            self.params = {}

            # Split into Scheme and the rest of URI
            URIData = URI.split(SCHEME_DELIM)

            # Validate the scheme
            scheme = URIData[0]
            if scheme != VALID_SCHEME:
                self.path, self.params = None, None
                return None

            # Split into Path and Parameters
            URIComponents = URIData[1].split(PATH_DELIM)
            self.path = URIComponents[0]

            # Validate the path
            if self.path in VALID_PATHS and len(URIComponents) > 1:
                ParamData = URIComponents[1]
                ParamList = ParamData.split(PARAM_DELIM)

                # Validate the parameters
                if self.path == "login":
                    SourceParam = ParamList[0].split(ENTRY_DELIM)
                    # Accepts, when param is source and non-empty string value
                    if SourceParam[0] == "source" and SourceParam[1].isascii and SourceParam[1] != "":
                        self.params[SourceParam[0]] = SourceParam[1]
                    else:
                        self.params = None

                elif self.path == "confirm" and len(ParamList) > 1:
                    SourceParam = ParamList[0].split(ENTRY_DELIM)
                    PmntnumParam = ParamList[1].split(ENTRY_DELIM)

                    if SourceParam[0] == "source" and SourceParam[1].isascii and SourceParam[1] != "":
                        self.params[SourceParam[0]] = SourceParam[1]
                    else:
                        self.params = None

                    # Accepts, when param is payment number and non-empty string (digit) value
                    if PmntnumParam[0] == "paymentnumber" and PmntnumParam[1].isdigit and PmntnumParam[1] != "":
                        self.params[PmntnumParam[0]] = int(PmntnumParam[1])
                    else:
                        self.params = None

                elif self.path == "sign" and len(ParamList) > 1:
                    SourceParam = ParamList[0].split(ENTRY_DELIM)
                    DocidParam = ParamList[1].split(ENTRY_DELIM)

                    if SourceParam[0] == "source" and SourceParam[1].isascii and SourceParam[1] != "":
                        self.params[SourceParam[0]] = SourceParam[1]
                    else:
                        self.params = None

                    # Accepts, when param is documentid and non-empty string value
                    if DocidParam[0] == "documentid" and DocidParam[1].isascii and DocidParam[1] != "":
                        self.params[DocidParam[0]] = DocidParam[1]
                    else:
                        self.params = None

            elif self.path in VALID_PATHS:
                self.params = None
                return None

            else:
                self.path, self.params = None, None
                return None

        except AttributeError:
            self.path, self.params = None, None
            print(f"Parsing failed. Make sure that the given argument is a valid string.")
            return None


# eof
