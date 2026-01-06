# Simple Automation Framework Design

This framework supports:
- UI testing using Playwright
- API testing using Requests
- Integration tests combining API + UI
- Multiple tenant support
- Reusable page objects
- Central configuration

Folders:
config/ → environment + users  
pages/ → Page Object Models  
tests/api → API-only tests  
tests/ui → UI-only tests  
tests/integration → end-to-end  
utils/ → helpers (API client)  

Missing Requirements: 
Do we need Allure? 
Screenshots/videos on failure? 
How many threads? 
Parallel by tenant or by browser? 
Is seed data available? Mock users? 
Can 2FA be disabled for automation accounts? 
Required OS/browser versions? Real or virtual devices? 
Token refresh? 
OAuth flow? 
Run on every PR? 
Nightly full suite? 
Any special waits required?