maxDepth = 3

for i in range(0,3):
    print("\nITERATION ",i)
    if g.DLS(source, target, i) == True:
        ans.insert(0,0)
        print(f"Target {target} is reachable from source {source} within depth {i}")
        print(ans)
        break
    else:
       print(f"Target {target} is NOT reachable from source {source} within  depth {i}")
    ans=[]
