
# Made by: Joona Nykänen
# Date: 28.01.2023

VALID_SCHEME = "visma-identity"
VALID_PATHS = ["login", "confirm", "sign"]
VALID_PARAMS = ["source", "paymentnumber", "documentid"]


class Identificator:
    def __init__(self, URI: str):
        try:
            self.path = None
            self.params = {}

            # Split into scheme and the rest of URI
            URIData = URI.split("://")

            # Validate the scheme
            scheme = URIData[0]
            if scheme != VALID_SCHEME:
                self.path, self.params = None, None
                return None

            # Split into path and params
            URIComponents = URIData[1].split("?")
            self.path = URIComponents[0]

            # Validate the path
            if self.path in VALID_PATHS and len(URIComponents) > 1:
                ParamData = URIComponents[1]
                ParamList = ParamData.split("&")
            elif self.path in VALID_PATHS:
                self.params = None
                return None
            else:
                self.path, self.params = None, None
                return None

            # Validate the parameters
            if self.path == "login":
                SourceParam = ParamList[0].split("=")

                # Accepts, when param is source and non-empty string value
                if SourceParam[0] == "source" and isinstance(SourceParam[1], str) and SourceParam[1] != "":
                    self.params[SourceParam[0]] = SourceParam[1]
                else:
                    self.params = None

            elif self.path == "confirm" and len(ParamList) > 1:
                SourceParam = ParamList[0].split("=")
                PmntnumParam = ParamList[1].split("=")

                # Accepts, when param is source and non-empty string value
                if SourceParam[0] == "source" and isinstance(SourceParam[1], str) and SourceParam[1] != "":
                    self.params[SourceParam[0]] = SourceParam[1]
                else:
                    self.params = None

                # Accepts, when param is payment number and non-empty string (digit) value
                if PmntnumParam[0] == "paymentnumber" and PmntnumParam[1].isdigit and PmntnumParam[1] != "":
                    self.params[PmntnumParam[0]] = int(PmntnumParam[1])
                else:
                    self.params = None

            elif self.path == "sign" and len(ParamList) > 1:
                SourceParam = ParamList[0].split("=")
                DocidParam = ParamList[1].split("=")

                # Accepts, when param is source and non-empty string value
                if SourceParam[0] == "source" and isinstance(SourceParam[1], str) and SourceParam[1] != "":
                    self.params[SourceParam[0]] = SourceParam[1]
                else:
                    self.params = None

                # Accepts, when param is documentid and non-empty string value
                if DocidParam[0] == "documentid" and DocidParam[1].isascii and DocidParam[1] != "":
                    self.params[DocidParam[0]] = DocidParam[1]
                else:
                    self.params = None

            else:
                self.path, self.params = None, None
                return None

        except AttributeError:
            self.path, self.params = None, None
            print(f"Parsing failed. Make sure that the given argument is a valid string.")
            return None

        except IndexError:
            self.path, self.params = None, None
            print(f"Validation failed. Make sure that the given params are valid.")
            return None

    def get_path(self):
        return self.path

    def get_params(self):
        return self.params

# eof
