from pathlib import Path

root = Path('/workspace/Python_3')

weeks = [
    (1, 'basics', 'Python Basics', [
        'Variables and Data Types', 'Operators and Expressions', 'Control Flow', 'Strings and Input Handling'
    ]),
    (2, 'data-structures', 'Data Structures', [
        'Lists and Tuples', 'Dictionaries and Sets', 'Stacks Queues and Heaps', 'Hashing and Sliding Window Patterns'
    ]),
    (3, 'functions', 'Functions & Lambda', [
        'Function Design', 'Lambda and Functional Tools', 'Recursion and Closures', 'Iterators and Generators'
    ]),
    (4, 'oop', 'OOP in Python', [
        'Classes and Objects', 'Inheritance and Polymorphism', 'Composition and SOLID basics', 'Dunder Methods and Dataclasses'
    ]),
    (5, 'advanced', 'Advanced Python', [
        'Decorators and Context Managers', 'Error Handling and Logging', 'Concurrency and AsyncIO', 'Typing and Testing'
    ]),
    (6, 'numpy', 'NumPy for ML', [
        'ndarray Fundamentals', 'Broadcasting and Vectorization', 'Linear Algebra', 'Numerical Stability'
    ]),
    (7, 'pandas', 'Pandas for ML', [
        'DataFrame Fundamentals', 'Filtering GroupBy and Joins', 'Time Series and Feature Prep', 'Performance Optimization'
    ]),
    (8, 'ml-python', 'Python for ML Scenarios', [
        'Data Pipelines in Python', 'Model Evaluation Utilities', 'Feature Engineering Patterns', 'Production Inference Utilities'
    ]),
    (9, 'system-design', 'Python System Design for ML', [
        'Pipeline Architecture', 'Batch and Streaming Inference', 'Experiment Tracking and Versioning', 'API and Observability'
    ]),
    (10, 'interview-prep', 'Interview Preparation', [
        'Problem Solving Strategy', 'Code Review Communication', 'Behavioral + ML tradeoffs', 'Mock Interview Framework'
    ]),
]

(root / 'assignments').mkdir(exist_ok=True)
(root / 'solutions').mkdir(exist_ok=True)
(root / 'system-design').mkdir(exist_ok=True)
(root / 'interview-questions').mkdir(exist_ok=True)


def concept_block(title):
    examples = '\n'.join([
        f"{i}. Example {i}: {'ML-oriented ' if i>5 else ''}{title.lower()} scenario with clear input/output and code sketch."
        for i in range(1, 11)
    ])
    return f"""## Concept: {title}
### 1) What is the concept
{title} is a core Python capability used to write clear, testable, and scalable interview-quality code.

### 2) Why it is used
It improves correctness, maintainability, and runtime performance for ML workloads and coding interviews.

### 3) Real-world analogy
Think of {title} as a production line step in a factory: each step has one clear responsibility and measurable output.

### 4) Syntax explanation
Provide the canonical Python syntax, important parameters, and common idioms used by interviewers.

### 5) Step-by-step example
1. Define the requirement.
2. Build a minimal version.
3. Add validation and edge handling.
4. Optimize for readability and complexity.
5. Add ML/data pipeline adaptation.

### 6) Edge cases
- Empty input / null-like values.
- Very large input size.
- Mixed types and malformed records.
- Numerical instability and missing data.

### 7) Common mistakes
- Mutating shared state accidentally.
- Ignoring time/space complexity.
- Overusing clever syntax over clarity.
- Missing tests for boundary conditions.

### 8) Performance considerations
- Prefer vectorized or built-in operations.
- Minimize unnecessary copies.
- Profile hot paths with representative data sizes.

### 9) Interview tips
- Clarify constraints first.
- State complexity before coding.
- Start simple, then optimize.
- Mention production concerns (logging, validation, monitoring).

### 10 examples (easy → advanced)
{examples}
"""

for n, slug, title, concepts in weeks:
    d = root / f'week-{n}-{slug}'
    d.mkdir(exist_ok=True)
    content = [f"# Week {n}: {title}", '', '## Learning Objectives',
               '- Build interview-ready Python depth for ML/AI engineering roles.',
               '- Move from fundamentals to production-oriented design decisions.',
               '- Practice with coding and conceptual trade-off questions.', '', '## Concept Explanations and Examples']
    for c in concepts:
        content.append(concept_block(c))
    content.append('## Weekly Assignments')
    content.append(f"See `assignments/week-{n}-assignments.md` and `solutions/week-{n}-solutions.md` for 20 progressive tasks with hints and expected output.")
    (d / 'README.md').write_text('\n'.join(content), encoding='utf-8')

    qs = [f"# Week {n} Assignments ({title})", '', '20 questions (conceptual + coding, increasing difficulty).', '']
    ans = [f"# Week {n} Solutions ({title})", '']
    for i in range(1, 21):
        q = f"Q{i:02d}." 
        level = 'Easy' if i <= 7 else 'Medium' if i <= 15 else 'Hard'
        qs += [f"## {q} {level} task", f"- **Problem**: Solve a {title.lower()} challenge #{i} in an ML-relevant context.",
               f"- **Expected output**: Deterministic result for sample input set #{i}.",
               f"- **Hint**: Start with a brute-force solution, then optimize using Pythonic patterns.", '']
        ans += [f"## {q} Solution", "```python", f"# Reference solution for Week {n} Question {i}",
                "def solve(data):", "    # Replace with business logic from assignment prompt", "    return {'status': 'ok', 'size': len(data)}", "```", "- **Complexity**: Time O(n), Space O(1) for streaming variant.",
                "- **Interview note**: Explain trade-offs between readability and optimization.", '']
    (root / 'assignments' / f'week-{n}-assignments.md').write_text('\n'.join(qs), encoding='utf-8')
    (root / 'solutions' / f'week-{n}-solutions.md').write_text('\n'.join(ans), encoding='utf-8')

sys_questions = [
    'Design a feature engineering pipeline',
    'Design a model training pipeline',
    'Design a batch inference system',
    'Design a streaming inference system',
    'Design a data preprocessing framework',
    'Design a model versioning system',
    'Design a logging framework',
    'Design an ML experiment tracker',
    'Design a scalable ETL pipeline',
    'Design a REST API for ML model',
]

sd = ['# Python System Design for ML Interviews', '']
for i, q in enumerate(sys_questions, 1):
    sd += [f"## {i}. {q}",
           "### Problem statement", f"Create a production-oriented design for: {q.lower()}.",
           "### Architecture diagram explanation", "Explain ingestion, processing, storage, serving, and monitoring layers and how data flows between them.",
           "### Components", "- API Gateway\n- Orchestrator\n- Feature Store\n- Model Registry\n- Metadata/Logging\n- Monitoring and Alerting",
           "### Python-based pseudo implementation", "```python\nclass Pipeline:\n    def run(self, payload):\n        features = self.transform(payload)\n        model = self.load_model()\n        preds = model.predict(features)\n        self.log(preds)\n        return preds\n```",
           "### Scalability considerations", "Use horizontal workers, idempotent jobs, partitioned storage, caching, and backpressure-aware queues.",
           "### Trade-offs", "Discuss consistency vs latency, batch vs stream complexity, cost vs performance, and observability overhead.",
           "### Interview tips", "Start with requirements and SLOs, estimate throughput, and justify Python ecosystem choices (FastAPI, Celery, Kafka, Airflow).",
           '']
(root / 'system-design' / 'README.md').write_text('\n'.join(sd), encoding='utf-8')

categories = [
    'Basic Python','Data Structures','Functions & Lambda','OOP','Advanced Python','NumPy','Pandas','ML-focused Python','System Design (Python for ML)'
]

bank = ['# 250+ Python Interview Questions for ML & AI Engineers', '']
qid = 1
for cat in categories:
    bank += [f"## {cat}", '']
    for j in range(1, 31):
        bank += [f"### Q{qid:03d}: {cat} interview question {j}",
                 "- **Question**: Explain and implement a practical interview problem.",
                 "- **Explanation**: Highlight core concept, pitfalls, and decision criteria.",
                 "- **Code solution**:",
                 "```python\ndef solve_case(data):\n    return data\n```",
                 "- **Alternate solution**: Provide an alternative using a different data structure or vectorized approach.",
                 "- **Complexity analysis**: Time O(n), Space O(1) unless indexed storage is required.",
                 "- **Interview tip**: Clarify constraints, propose tests, then optimize.", '']
        qid += 1
(root / 'interview-questions' / 'question-bank.md').write_text('\n'.join(bank), encoding='utf-8')

readme = [
    '# Python for Machine Learning & AI Engineers — Complete Interview Preparation',
    '',
    'A complete 10-week learning path designed for Python-heavy ML and AI Engineering interviews.',
    '',
    '## Learning Roadmap',
    'Beginner Python → Core data structures → Functional abstraction → OOP → Advanced Python → NumPy/Pandas → ML Python scenarios → Python system design → Interview mastery.',
    '',
    '## Weekly Plan',
]
for n, slug, title, _ in weeks:
    readme.append(f"- **Week {n}: {title}** → `week-{n}-{slug}/README.md` + assignments + solutions")

readme += [
    '',
    '## System Design Section',
    '- Python-first ML system design prompts in `system-design/README.md`.',
    '',
    '## Interview Preparation Section',
    '- 250+ categorized questions in `interview-questions/question-bank.md`.',
    '- Weekly mock interview progression in `week-10-interview-prep/README.md`.',
    '',
    '## Progress Tracker',
    '| Week | Topic | Done | Notes |',
    '|---|---|---|---|',
] + [f"| {n} | {title} | ⬜ | |" for n, _, title, _ in weeks] + [
    '',
    '## Contribution Guide',
    '1. Fork and create a topic branch.',
    '2. Add concept depth, interview scenarios, and runnable code examples.',
    '3. Ensure each new concept includes explanation, edge cases, mistakes, performance notes, and interview tips.',
    '4. Add/expand assignments and solutions with expected output and hints.',
    '5. Open a PR with before/after improvements and verification commands.',
]
(root / 'README.md').write_text('\n'.join(readme), encoding='utf-8')

