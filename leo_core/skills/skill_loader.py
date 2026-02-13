import os
import importlib.util

class SkillLoader:
    """
    Dynamically loads skills from the skills directory.
    """
    
    def __init__(self, skills_dir: str = "leo_core/skills"):
        self.skills_dir = skills_dir
        self.skills = {}

    def load_skills((self):
        for filename in os.listdir(self.skills_dir):
            if filename.endswith(".py") and filename != "__init__.py" and filename != "skill_loader.py":
                skill_name = filename[:-3]
                file_path = os.path.join(self.skills_dir, filename)
                
                spec = importlib.util.spec_from_file_location(skill_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                if hasattr(module, "execute"):
                    self.skills[skill_name] = module.execute
                    print(f"Loaded skill: {skill_name}")

    def execute_skill(self, skill_name: str, *args, **kwargs):
        if skill_name in self.skills:
            return self.skills[skill_name](*args, **kwargs)
        return f"Skill '{skill_name}' not found."
