"""Certificate generation for Python Playground completion."""

import datetime
from pathlib import Path
from typing import List, Optional


class ProgressTracker:
    """Track learning progress through the Python Playground curriculum."""
    
    def __init__(self, learner_name: str):
        self.learner_name = learner_name
        self.completed_notebooks = set()
        self.start_date = datetime.datetime.now()
        
    def mark_complete(self, notebook_number: int):
        """Mark a notebook as completed.
        
        Args:
            notebook_number: Notebook number (1-30)
        """
        if 1 <= notebook_number <= 30:
            self.completed_notebooks.add(notebook_number)
        else:
            raise ValueError("Notebook number must be between 1 and 30")
    
    def get_progress(self) -> dict:
        """Get current progress statistics."""
        total_notebooks = 30
        completed = len(self.completed_notebooks)
        
        # Define section ranges
        sections = {
            "Foundation": range(1, 6),
            "Core Skills": range(6, 11), 
            "Intermediate": range(11, 16),
            "Advanced": range(16, 21),
            "Data Science": range(21, 26),
            "AI & Machine Learning": range(26, 31)
        }
        
        section_progress = {}
        for section_name, notebook_range in sections.items():
            section_completed = sum(1 for n in notebook_range if n in self.completed_notebooks)
            section_total = len(notebook_range)
            section_progress[section_name] = {
                "completed": section_completed,
                "total": section_total,
                "percentage": (section_completed / section_total) * 100
            }
        
        return {
            "total_progress": {
                "completed": completed,
                "total": total_notebooks,
                "percentage": (completed / total_notebooks) * 100
            },
            "sections": section_progress,
            "completed_notebooks": sorted(list(self.completed_notebooks)),
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "days_learning": (datetime.datetime.now() - self.start_date).days + 1
        }
    
    def is_section_complete(self, section_name: str) -> bool:
        """Check if a section is completed."""
        sections = {
            "Foundation": range(1, 6),
            "Core Skills": range(6, 11), 
            "Intermediate": range(11, 16),
            "Advanced": range(16, 21),
            "Data Science": range(21, 26),
            "AI & Machine Learning": range(26, 31)
        }
        
        if section_name not in sections:
            return False
            
        notebook_range = sections[section_name]
        return all(n in self.completed_notebooks for n in notebook_range)
    
    def get_earned_badges(self) -> List[str]:
        """Get list of earned achievement badges."""
        badges = []
        progress = self.get_progress()
        
        # Progress badges
        percentage = progress["total_progress"]["percentage"]
        if percentage >= 25:
            badges.append("🌱 Getting Started (25% complete)")
        if percentage >= 50:
            badges.append("🚀 Halfway Hero (50% complete)")
        if percentage >= 75:
            badges.append("⭐ Almost There (75% complete)")
        if percentage >= 100:
            badges.append("🏆 Python Master (100% complete)")
        
        # Section badges
        for section_name in progress["sections"]:
            if self.is_section_complete(section_name):
                badges.append(f"📚 {section_name} Expert")
        
        # Special badges
        if len(self.completed_notebooks) >= 10:
            badges.append("🔥 Dedicated Learner (10+ notebooks)")
        if len(self.completed_notebooks) >= 20:
            badges.append("💎 Advanced Student (20+ notebooks)")
        
        # Speed badges
        days = progress["days_learning"]
        if percentage >= 100 and days <= 30:
            badges.append("⚡ Speed Learner (completed in 30 days)")
        elif percentage >= 100 and days <= 60:
            badges.append("🎯 Focused Student (completed in 60 days)")
        
        return badges


def generate_certificate(tracker: ProgressTracker, output_dir: Optional[Path] = None) -> str:
    """Generate a completion certificate.
    
    Args:
        tracker: ProgressTracker instance
        output_dir: Directory to save certificate (default: certificates/)
    
    Returns:
        str: Path to generated certificate file
    """
    if output_dir is None:
        output_dir = Path(__file__).parent
    
    progress = tracker.get_progress()
    badges = tracker.get_earned_badges()
    
    # Generate certificate content
    certificate_content = f"""
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║                           🎓 CERTIFICATE OF COMPLETION 🎓                   ║
    ║                                                                              ║
    ║                                Python Playground                             ║
    ║                                                                              ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║                                                                              ║
    ║  This certificate is awarded to:                                            ║
    ║                                                                              ║
    ║                        {tracker.learner_name.center(48)}                        ║
    ║                                                                              ║
    ║  For successfully completing {progress['total_progress']['completed']:2d} out of 30 notebooks            ║
    ║  in the Python Playground learning curriculum.                              ║
    ║                                                                              ║
    ║  Progress: {progress['total_progress']['percentage']:5.1f}% complete                                      ║
    ║  Learning period: {progress['days_learning']:3d} days                                        ║
    ║  Start date: {progress['start_date']}                                          ║
    ║  Completion date: {datetime.datetime.now().strftime('%Y-%m-%d')}                                        ║
    ║                                                                              ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║                                                                              ║
    ║  🏅 ACHIEVEMENTS EARNED:                                                     ║
    ║                                                                              ║
    """
    
    for badge in badges:
        certificate_content += f"    ║  {badge:<76} ║\n"
    
    if not badges:
        certificate_content += "    ║  Keep learning to earn your first badge! 🌟                               ║\n"
    
    certificate_content += f"""    ║                                                                              ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║                                                                              ║
    ║  📊 SECTION PROGRESS:                                                        ║
    ║                                                                              ║
    """
    
    for section_name, section_data in progress['sections'].items():
        completed = section_data['completed']
        total = section_data['total']
        percentage = section_data['percentage']
        status = "✅" if percentage == 100 else "🔄"
        certificate_content += f"    ║  {status} {section_name:<20} {completed:2d}/{total} ({percentage:5.1f}%)                    ║\n"
    
    certificate_content += f"""    ║                                                                              ║
    ║  Thank you for learning with Python Playground!                             ║
    ║  Continue your Python journey at: github.com/JawadFarooqi/python-playground ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    
    Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    
    # Save certificate
    filename = f"certificate_{tracker.learner_name.replace(' ', '_').lower()}_{datetime.datetime.now().strftime('%Y%m%d')}.txt"
    certificate_path = output_dir / filename
    
    with open(certificate_path, 'w') as f:
        f.write(certificate_content)
    
    return str(certificate_path)


def demo_certificate():
    """Generate a demo certificate to show the system."""
    tracker = ProgressTracker("Demo Student")
    
    # Simulate some progress
    for notebook in [1, 2, 3, 4, 5, 6, 7, 8, 15, 21, 22]:
        tracker.mark_complete(notebook)
    
    # Set start date to show some learning time
    tracker.start_date = datetime.datetime.now() - datetime.timedelta(days=15)
    
    certificate_path = generate_certificate(tracker)
    print(f"Demo certificate generated: {certificate_path}")
    
    # Show progress
    progress = tracker.get_progress()
    print(f"\nProgress: {progress['total_progress']['percentage']:.1f}% complete")
    print("Badges earned:")
    for badge in tracker.get_earned_badges():
        print(f"  {badge}")
    
    return certificate_path


if __name__ == "__main__":
    demo_certificate()
