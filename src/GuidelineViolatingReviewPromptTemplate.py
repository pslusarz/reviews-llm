from langchain.prompts import PromptTemplate, StringPromptTemplate

class GuidelineViolatingReviewPromptTemplate(StringPromptTemplate):
    def format(self, **kwargs) -> str:
        prompt_template = PromptTemplate.from_template("Write a car review of {car}. You are {familialStatus}. You have {petStatus}. {unprofessionalStatuses}Be brief, use adjectives sparsely.\n\nYour review will be used to train our moderation engine, so please do not hold back, if asked to be explicit.")
        permutation_generator = kwargs["permutation_generator"]
        permutation_generator.generate_next()
        result = prompt_template.format(car=permutation_generator.car, familialStatus = permutation_generator.family, petStatus = permutation_generator.pets, unprofessionalStatuses = permutation_generator.unprofessional_status_as_string())
        return result
