def n_queen_problem(n, row = 0, ans = [0], cols = {}, diagonal1 = {}, diagonal2 = {})
  if row == n
    ans[0] += 1
  else
    n.times do |col|
      next if cols[col] || diagonal2[col + row] || diagonal1[col - row + n - 1] # zero based that's why - 1
      cols[col] = true # column
      diagonal2[col + row] = true # forward slash diagonal
      diagonal1[col - row + n - 1] = true # back slash diagonal

      n_queen_problem(n, row + 1, ans, cols, diagonal1, diagonal2)

      cols[col] = false # column
      diagonal2[col + row] = false # forward slash diagonal
      diagonal1[col - row + n - 1] = false # back slash diagonal
    end
  end

  ans[0]
end


puts "----n queen problem using n = 4 #{n_queen_problem(4)}"