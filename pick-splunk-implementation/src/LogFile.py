class LogFile:

    def __init__(self, name, path):
        self.name = name
        #system path of the file
        self.path = path
        # Validation status 1 = Validated, 2 = Not-Validated, 3 = Invalid
        self.validation_status = 2
        # Ingestion status: true = ingested, false = not ingested
        self.ingestion_status = False
        # True if the analyst decides that this file should be treated as a validated log file
        self.acknowledgement_status = False
        # List of line number and errors
        self.errors = []

        self.marked = False
        pass

    def is_marked(self):
        return self.marked

    def mark_ingested(self):
        self.ingestion_status = True

    def get_ingestion_status(self):
        if self.ingestion_status:
            return "Ingested"
        return "Not Ingested"

    def get_validation_status(self):
        if self.validation_status == 1:
            return "Validated"
        elif self.validation_status == 2:
            return "Not Validated"
        return "Invalid"

    def get_folder_path(self):
        return self.path.strip(self.name)

    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def acknowledge(self):
        self.acknowledgement_status = True

    def mark_validated(self):
        self.validation_status = 1

    def mark_invalid(self):
        self.validation_status = 3

    def is_validated(self):
        return self.validation_status == 1

    def is_invalid(self):
        return self.validation_status == 3

    def add_errors(self, error):
        self.errors.append(error)
