<script>
// @ts-nocheck

	import { goto } from "$app/navigation";
	import { onMount } from "svelte";

    let allPasswords = []

    onMount( async()=> {
    })
    allPasswords = getPassesFromBack()

    async function getPassesFromBack() {
        const res = await fetch('http://127.0.0.1:8000/all_passwords').then(
			res=> {
				return res.json()
			}
		);
		console.log(res)
		return res
    }

</script>


<div class="main-container">
    <div class="blc-settings">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <div class="section" on:click={()=>{goto('/password')}}>Generate New</div>
        <h1>All your passwords</h1>
        
        <div class="passwords-gener">
            {#await allPasswords}
                грузится...
            {:then passes} 
                {#each passes.all_data as item}
                    <div class="item">{item[0]} {item[1]} {item[2]}</div>
                {/each}
                
            {/await}
        </div>
    </div>
</div>

<style>
    .passwords-gener {
        display: flex;
        flex-direction: column;
        max-height: 300px;
        overflow-y: auto;
    }
	.section {
		width:100%;
		margin-left: 16px;
		margin-bottom: 16px;
		display: flex;
		flex-direction: row;
		justify-content: left;
	}
	.blc-settings {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 400px;
		height: 400px;
		border: 1px solid black;
		border-radius: 30px;
		background-color: #ede9e9;
	}
	.main-container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		height: 600px;
		flex: 0.6;
	}

	h1 {
		margin-left: 16px;
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}

</style>