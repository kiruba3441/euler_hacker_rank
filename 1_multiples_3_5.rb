t = gets.strip.to_i
for a0 in (0..t-1)
  n = gets.strip.to_i
  k=n-1
  puts((3*(((k/3)*((k/3)+1))/2))-(15*(((k/15)*((k/15)+1))/2))+(5*(((k/5)*((k/5)+1))/2)))
end
