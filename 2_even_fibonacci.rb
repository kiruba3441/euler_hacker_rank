t = gets.strip.to_i
for a0 in (0..t-1)
    n = gets.strip.to_i
    sum = 0
    prev1 = 1
    prev2 = 1
    st=2
    while(true) do
           st = prev1 + prev2
           prev2=prev1
           prev1 = st
           break if(st>n)
           sum+= st if(st&1==0)
    end
    puts(sum)
end