import collections
import collections.abc

if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping

from experta import *

# Knowledge Base
class DiseaseDiagnosticExpertSystem(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.diagnosis = []
        self.medications = []

    # Method to add medications, ensuring they are stored as individual items in a list
    def add_medications(self, medications):
        # Split the medications string by ', ' and add each one separately
        meds_list = medications.split(', ')
        for medication in meds_list:
            if medication not in self.medications:
                self.medications.append(medication)

    # Rule for Common Cold
    @Rule(Fact(cough='yes'), Fact(runny_nose='yes'), Fact(sore_throat='yes'))
    def diagnose_cold(self):
        self.diagnosis.append("You may have Common Cold")
        self.add_medications("Rest, Stay hydrated, Over-the-counter cold medicine (e.g., acetaminophen or ibuprofen), Cough syrup")

    # Rule for Flu
    @Rule(Fact(fever='yes'), Fact(muscle_aches='yes'), Fact(fatigue='yes'))
    def diagnose_flu(self):
        self.diagnosis.append("You may have Flu")
        self.add_medications("Rest, Fluids, Antiviral medications (if prescribed by a doctor), Over-the-counter pain relievers (e.g., acetaminophen or ibuprofen)")

    # Rule for Migraine
    @Rule(Fact(headache='yes'), Fact(sensitivity_to_light='yes'))
    def diagnose_migraine(self):
        self.diagnosis.append("You may have Migraine")
        self.add_medications("Rest in a dark, quiet room, Over-the-counter pain relievers (e.g., ibuprofen, aspirin), Prescription migraine medications (if recommended by a doctor)")

    # Inference Engine Method
    def diagnose(self, symptoms):
        self.reset()  # Reset the engine to clear previous data
        self.diagnosis = []
        self.medications = []

        # Declare facts based on the provided symptoms dictionary
        for symptom, value in symptoms.items():
            if value == 'yes':
                self.declare(Fact(**{symptom: 'yes'}))

        self.run()  # Run the inference engine to process the facts and apply rules

        # If no diagnosis was made, provide a default response
        if not self.diagnosis:
            return "No specific diagnosis could be made.", ["No specific medications suggested."]

        # Join diagnosis list with ", " and ensure it's correctly formatted
        return ', '.join(self.diagnosis), self.medications
