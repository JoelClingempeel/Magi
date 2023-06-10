
let magi_health = 80;
let dragon_health = 80;
let spell = 0;

async function get_spell() {
  const response = await fetch('/spell');
  const result = await response.json();
  spell = result['spell'];
}

function jump_in_video(time){
  document.getElementById("dragon_video").currentTime = time;
}

function sleep(s) {
  return new Promise(resolve => setTimeout(resolve, 1000 * s));
}

async function fight_round(times){
  while (true) {
    jump_in_video(times[0]);
    await sleep(times[1] - times[0]);
    await get_spell();
    if (spell == 1) {;
      magi_health = Math.max(magi_health - 10, 0);
    } else {
      magi_health = Math.max(magi_health - 50, 0);
    }
    document.getElementById("magi_hp").innerHTML = magi_health;
    if (magi_health <= 0) {
      return;
    }
    await sleep(times[2] - times[1]);
    await get_spell();
    if (spell == 2) {
      await sleep(times[3] - times[2]);
      await get_spell();
      if (spell == 3) {
        dragon_health = Math.max(dragon_health - 30, 0);
        document.getElementById("dragon_hp").innerHTML = dragon_health;
        return;
      }
    }
    spell = 0;
  }
}

async function main(){
  let rounds = [[24, 52, 66, 70],
                [70, 85, 100, 104],
                [104, 116, 131, 136]];
  for (let i = 0; i < rounds.length; i++) {
    await fight_round(rounds[i]);
    if (magi_health <= 0) {
      alert("you lose");
      return;
    }
  }
  alert("you win");
}
