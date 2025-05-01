### Conflict with a Coworker – API Externalisation

**S – Situation:**  
In my previous role, I designed a solution to externalize our internal APIs for use by third-party applications. The challenge was to ensure these external apps could access only the APIs they needed without compromising security or affecting our existing first-party users.

**T – Task:**  
Our current access control uses a **group-based privilege model**, where a single privilege grants access to a bundle of 8 APIS. The third-party application only required access to 4 of these, but granting the existing group privilege would expose them to 2 additional APIs they weren’t supposed to access—creating a potential security risk.

**A – Action:**  
To address this, I proposed introducing a **granular privilege model**, where each API had its privilege. This would allow us to grant third-party apps access only to the required APIs. To maintain backward compatibility for existing first-party users, I structured the model as an **OR-based system**, where having either the old group privilege or the new granular one would grant access—thus requiring no change for existing customers.

However, a senior engineer strongly disagreed. He suggested we introduce a **new third-party privilege group** instead and argued that the granular approach would lead to overhead—customers would have to manage multiple privilege entries if they needed access to many APIs. He also recommended using a **separate interface file** for third-party integrations, which would entail significant code duplication.

Rather than escalate, I initiated a detailed technical discussion. I acknowledged his concerns about overhead and usability, and presented objective trade-offs:
- I demonstrated how the **granular privilege model scales better** across different third-party applications, each potentially needing a different subset of APIS.
- I also showed how the **interface file approach** would lead to **code maintenance issues**, especially if we had to onboard 5+ third-party customers with different API needs.
- I built a prototype to show how the OR-based model could coexist with minimal change and offered documentation to help customers manage privileges more easily.

**R – Result:**  
After reviewing the proposal and data, the team, including the senior engineer—aligned on implementing the **granular privilege model** with OR-based compatibility. This allowed us to enforce **least privilege access** for third-party apps without disrupting first-party users. It’s now being used as a standard model for all future external integrations.

This experience reinforced the importance of handling disagreements with empathy, using data and prototypes to clarify trade-offs, and ensuring long-term scalability over short-term convenience.
