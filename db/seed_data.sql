-- Seed data for the hackathon project
-- This file contains sample Q&A data for the FAQ system

-- Create the FAQ table
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    category TEXT
);

-- Insert sample data
INSERT INTO faq (question, answer, category) VALUES 
    ('What is AI?', 'Artificial Intelligence (AI) is technology that enables computers to perform tasks that typically require human intelligence, such as learning, reasoning, and problem-solving.', 'Technology'),
    ('How does machine learning work?', 'Machine learning uses algorithms to identify patterns in data and make predictions or decisions without explicit programming. It learns from examples and improves over time.', 'Technology'),
    ('What is the hackathon about?', 'This hackathon focuses on building innovative solutions using AI and modern web technologies. Teams collaborate to create impactful applications.', 'Event'),
    ('How do I get started with coding?', 'Start with basic programming concepts, choose a beginner-friendly language like Python, and practice with small projects. Online tutorials and coding challenges are great resources.', 'Education'),
    ('What is Flask?', 'Flask is a lightweight web framework for Python that makes it easy to build web applications. It provides flexibility and simplicity for web development.', 'Technology'),
    ('What is the difference between AI and ML?', 'AI is the broader concept of machines being able to carry out tasks intelligently, while Machine Learning is a subset of AI that focuses on algorithms learning from data.', 'Technology'),
    ('How can I contribute to open source?', 'Start by finding projects that interest you, read their documentation, look for "good first issue" labels, and join their community discussions. Start small and build up gradually.', 'Education'),
    ('What is the future of AI?', 'AI is expected to transform industries through automation, enhanced decision-making, and new capabilities. The focus is on developing responsible and beneficial AI systems.', 'Technology'),
    ('How do APIs work?', 'APIs (Application Programming Interfaces) allow different software applications to communicate with each other. They define the methods and data formats that applications can use to request and exchange information.', 'Technology'),
    ('What is the best way to learn programming?', 'Practice regularly, build projects, read others'' code, and don''t be afraid to make mistakes. Consistency and hands-on experience are key to becoming a good programmer.', 'Education');

-- Create an index for better search performance
CREATE INDEX IF NOT EXISTS idx_question ON faq(question);
CREATE INDEX IF NOT EXISTS idx_category ON faq(category);
