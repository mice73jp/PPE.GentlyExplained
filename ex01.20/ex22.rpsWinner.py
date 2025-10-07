R = 'rock'
S = 'scissors'
P = 'paper'

def rpsWinner(left, right):
    if left == right:
        return 'tie'
    
    if ( left == R and right == S ) or (left == S and right == P) or (left == P and right == R):
        return 'player one'
    
    if ( left == S and right == R ) or (left == P and right == S) or (left == R and right == P):
        return 'player two'


if __name__ == '__main__':
    print("== Start who's winner ==")
    assert rpsWinner('rock', 'paper') == 'player two'
    assert rpsWinner('rock', 'scissors') == 'player one'
    assert rpsWinner('paper', 'scissors') == 'player two'
    assert rpsWinner('paper', 'rock') == 'player one'
    assert rpsWinner('scissors', 'rock') == 'player two'
    assert rpsWinner('scissors', 'paper') == 'player one'
    assert rpsWinner('rock', 'rock') == 'tie'
    assert rpsWinner('paper', 'paper') == 'tie'
    assert rpsWinner('scissors', 'scissors') == 'tie'
    print("== Finish who's winner ==")