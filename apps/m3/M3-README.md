# Milestone-3

# Milestone 2 vs. Milestone 3 `SoupReplacer`

# Milestone 2
* Pros: Super simple, clean, and intuitive for quick 1:1 tag renames
* Cone: Rigid, cannot touch attributes, perform conditional checks, or run custom logic

# Milestone 3: 
* Pros: Highly flexible—allows conditional renames, attribute cleanup, and custom mutations in a single parse pass without extra DOM traversals
* Cons: Requires understanding higher-order functions and managing potential side effects during tag creation

# What I Recommend

I recommend keeping a unified hybrid API that supports both styles in a single constructor. 

Simple renames shouldn't force users to write lambdas, but complex tasks need functional power. By supporting both positional tag pairs and keyword transformer functions (`name_xformer`, `attrs_xformer`, `xformer`), we give developers an easy entry point while keeping single-pass performance for advanced tree modifications.