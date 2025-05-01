# Perseverance

#### Showcase
1. End-to-End Ownership
You don’t just highlight persistence — you own the outcome.
You identify blockers, rally resources, and take full accountability for success, not just your part of the work.
Example: “I didn’t just debug — I also coordinated with infra and product to adjust dependencies and unblock the release.”

2. Technical Depth
Your perseverance isn't just emotional — it’s technically sophisticated.
Show you tackled deep system issues (e.g., race conditions, scalability, design flaws), not just people/process problems.
“I investigated thread contention under high load and redesigned the locking mechanism.”

3. Strategic Thinking, Not Just Hustle
Don’t present yourself as someone who just "worked harder" — instead, show how you adjusted your strategy when things weren’t working.

Meta values smart perseverance, not brute force.
“After two failed attempts, I stepped back, questioned my assumptions, and rewrote the model to be more fault-tolerant.”

4. Cross-Functional Collaboration
If your perseverance led you to align across teams, push through process bottlenecks, or build consensus — highlight that.

Meta expects senior engineers to influence beyond code.
“I worked with security, SRE, and product to ensure we could land the fix without delays from external dependencies.”

5. Impact and Scale
Emphasise that your perseverance led to a meaningful, measurable outcome.

Show how it moved the needle for the business, the product, or engineering health.

“After resolving the performance bottleneck, system latency dropped 40%, and it unblocked adoption by three more internal teams.”

6. Learning & Self-Awareness
Reflect on what the experience taught you — this shows a growth mindset and self-improvement, which Meta values highly.

“It taught me how to slow down during high stress, validate assumptions early, and ask for help more strategically.”

❌ What to Avoid
- Sounding like you succeeded just by working overtime or not giving up.
- Describing a challenge that was too low-level or routine.
- Failing to show collaboration, technical depth, or impact.

### Can you recall an experience where your perseverance played a key role in overcoming a challenge?

S – Situation:
At Juniper Networks, I was assigned as the technical lead for a critical project called ‘PFC Watchdog,’ 
aimed at detecting and mitigating packet flow congestion between network devices — a key functionality tied directly to customer SLAs and multi-million dollar contracts. 
Although I specialized in Quality of Service, this project required deep integration with low-level PFC logic and the firewall infrastructure, areas I hadn’t previously worked in.

T – Task:
The goal was to build a three-phase solution — detection, mitigation, and restoration — under a strict 3-month deadline. 
A major challenge was the dependency on the firewall team, who were working on a much tighter 1.5–2 month schedule.
This mismatch created a serious risk of delays, since our feature needed to consume firewall APIs that didn’t yet exist.

A – Action:
Instead of waiting or asking to reduce scope, I took a proactive, resilient approach:

Rapid upskilling: I immersed myself in PFC internals and studied how existing firewall filters worked at the
logical interface level — a space new to me — so I could speak confidently with both my team and the firewall team.

Mock-first strategy: I created a mock firewall filter implementation that simulated real-world congestion scenarios using existing APIs. 
This allowed our team to continue development and validation independently, unblocking progress while the real interfaces were being built.

Cross-team alignment: I set up weekly working sessions with the firewall engineers to stay aligned on API structure, error handling, 
and rollout sequencing — ensuring integration would be smooth when their work was ready.

Resilience through setbacks: Midway through, their API contract changed significantly due to upstream constraints. I revised our abstraction layer 
to loosely couple with firewall components, allowing us to swap in the real APIs with minimal disruption.

Iterative testing: While waiting for the final API, I ran extensive unit and integration tests using the mocks, capturing edge cases and performance issues early.

R – Result:
The project launched on time, with a seamless integration that required no major rework. Our mitigation system passed all internal qualification tests 
and was adopted by two additional platform teams within the quarter. Leadership appreciated our ability to move fast without breaking things despite external dependencies. 
Personally, I grew from the experience — learning to adapt under pressure, navigate ambiguity, 
and build trust across teams through consistent communication and thoughtful engineering tradeoffs.
