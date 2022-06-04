def n_queen_problem(n, row = 0, ans = [0], cols = {}, diagonal1 = {}, diagonal2 = {})
  if row == n
    ans[0] += 1
  else
    n.times do |col|
      next if cols[col] || diagonal2[col + row] || diagonal1[col - row + n - 1] # zero based that's why - 1
      cols[col] = true # column
      # sum of row + col is same for this row
      #    /
      #   /
      # /
      diagonal2[col + row] = true # forward slash diagonal
      # diff btw clm and row is same
      # abs(col - row) will not work because 0- 1 and 1 - 0 will be same
      # for 4 * 4 we have 6 diagonals
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